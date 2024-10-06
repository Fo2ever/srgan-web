import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import seaborn as sns


def load_and_process_data():
    file1 = "data/summary_data/processing_results_af_gans.csv"
    file2 = "data/summary_data/processing_results_bf_gans.csv"

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    return df1, df2


def process_confidence_data(df, label):
    df["confidence"] = df["confidence"].apply(
        lambda x: x.strip("[]") if isinstance(x, str) else x
    )

    df["confidence"] = pd.to_numeric(df["confidence"], errors="coerce")

    df.dropna(subset=["confidence"], inplace=True)

    df["label"] = label
    # print(len(df))
    df["sample_image_count"] = len(df)

    return df


# -------------------------------------- callback ------------------------------------------
@dash.callback(
    Output("donut-chart", "figure"), Input("image-result-interval", "n_intervals")
)
def update_donut_chart(n_intervals):
    df1, df2 = load_and_process_data()

    memory_size_file1 = df1["memory_size"].sum()
    memory_size_file2 = df2["memory_size"].sum()

    labels = ["SRResGan", "NotGans"]
    sizes = [memory_size_file1, memory_size_file2]

    colors = ["#ff9999", "#66b3ff"]
    fig = go.Figure()
    fig.add_pie(labels=labels, values=sizes, hole=0.3, marker=dict(colors=colors))

    return fig


@dash.callback(
    Output("time-process-chart", "figure"),
    Input("image-result-interval", "n_intervals"),
)
def update_time_process_plot(n_intervals):
    df1, df2 = load_and_process_data()

    df1["processing_time_rolling"] = df1["processing_time"].rolling(window=10).mean()
    df2["processing_time_rolling"] = df2["processing_time"].rolling(window=10).mean()

    df1["label"] = "After Model"
    df2["label"] = "Before Model"

    combined_df = pd.concat(
        [
            df1[["processing_time_rolling", "label"]],
            df2[["processing_time_rolling", "label"]],
        ]
    )

    app = dash.Dash(__name__)

    fig = px.line(
        combined_df,
        x=combined_df.index,
        y="processing_time_rolling",
        color="label",
        title="Rolling Average Processing Time",
        labels={
            "processing_time_rolling": "Rolling Average Processing Time",
            "label": "Model",
        },
    )

    return fig


@dash.callback(
    Output("plot-confidence", "figure"),
    Input("image-result-interval", "n_intervals"),
)
def update_confidence_plot(n_intervals):
    df1, df2 = load_and_process_data()

    confidence_data_after = process_confidence_data(df1, "After")
    confidence_data_before = process_confidence_data(df2, "Before")

    combined_data = pd.concat([confidence_data_after, confidence_data_before])

    fig = go.Figure()
    if len(combined_data) > 0:
        fig.add_trace(
            go.Violin(
                x=combined_data["label"][combined_data["label"] == "After"],
                y=combined_data["confidence"][combined_data["label"] == "After"],
                name="After Model",
                box_visible=False,
                meanline_visible=True,
                points="all",
                jitter=0.05,
                marker=dict(opacity=0.6),
                line=dict(color="blue"),
            )
        )

        fig.add_trace(
            go.Violin(
                x=combined_data["label"][combined_data["label"] == "Before"],
                y=combined_data["confidence"][combined_data["label"] == "Before"],
                name="Before Model",
                box_visible=False,
                meanline_visible=True,
                points="all",
                jitter=0.05,
                marker=dict(opacity=0.6),
                line=dict(color="blue"),
            )
        )

        fig.add_trace(
            go.Box(
                x=combined_data["label"][combined_data["label"] == "After"],
                y=combined_data["confidence"][combined_data["label"] == "After"],
                name="Model A - Boxplot",
                boxmean=True,  # Show mean
                marker_color="blue",
                line_width=2,
                width=0.3,
            )
        )

        fig.add_trace(
            go.Box(
                x=combined_data["label"][combined_data["label"] == "Before"],
                y=combined_data["confidence"][combined_data["label"] == "Before"],
                name="Model B - Boxplot",
                boxmean=True,
                marker_color="green",
                line_width=2,
                width=0.3,
            )
        )

        fig.update_layout(
            title="Rain cloud plot with Mean for Confidence Values by Model",
            xaxis_title="Model",
            yaxis_title="Confidence",
        )

    return fig
