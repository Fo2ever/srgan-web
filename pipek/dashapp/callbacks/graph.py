import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import io
import base64
import numpy as np


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

    # สร้าง Donut Chart พร้อมเส้นลากชี้ label
    fig.add_pie(
        labels=labels,
        values=sizes,
        hole=0.7,  # ขนาดของรูตรงกลาง
        marker=dict(colors=colors),
        textinfo="label+percent",  # แสดง label พร้อมเปอร์เซ็นต์
        textposition="outside",  # ย้าย label ออกไปข้างนอก
        pull=[0.05, 0.05],  # ดึงแต่ละส่วนออกเล็กน้อย
        showlegend=False,  # ปิด legend
    )

    # ปรับ layout
    fig.update_layout(
        annotations=[
            dict(
                text="Memory Usage",  # ข้อความที่ต้องการแสดง
                x=0.5,  # ตำแหน่งแกน x ให้อยู่ตรงกลาง
                y=0.5,  # ตำแหน่งแกน y ให้อยู่ตรงกลาง
                font_size=20,  # ขนาดของฟอนต์
                showarrow=False,  # ไม่ต้องแสดงลูกศร
            )
        ],
        height=350,  # ปรับความสูงของกราฟ
        width=380,  # ปรับความกว้างของกราฟ
        margin=dict(t=20, b=20, l=20, r=20),  # ลด margin
    )

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
        title="Average Processing Time",
        labels={
            "processing_time_rolling": "Rolling Average Processing Time",
            "label": "Model",
        },
        line_shape="spline",  # ทำให้เส้นสมูท
    )

    fig.update_layout(
        plot_bgcolor="rgb(225, 230, 235)",  # พื้นหลังของกราฟ
        paper_bgcolor="#ffffff",  # พื้นหลังของพื้นที่นอกกราฟ
        font=dict(size=14, color="#252525"),  # ขนาดตัวอักษร  # สีตัวอักษร
        title=dict(
            font=dict(size=20), x=0.5, xanchor="center"  # ขนาดของหัวข้อกราฟ  # จัดกลาง
        ),
        xaxis=dict(
            title="Time",
            showgrid=True,  # เปิด gridline แนวนอน
            gridcolor="#e6e6e6",  # สีของ gridline ให้ดูอ่อน
            zeroline=False,  # ไม่แสดงเส้นแกนศูนย์
        ),
        yaxis=dict(
            title="Processing Time", showgrid=True, gridcolor="#e6e6e6", zeroline=False
        ),
        legend=dict(
            title="Model",  # ปรับชื่อ legend
            orientation="h",  # ทำให้ legend เป็นแนวนอน
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
        ),
    )
    fig.for_each_trace(
        lambda trace: trace.update(
            line=dict(
                color={
                    "After Model": "#ff9999",  # สีชมพูสำหรับ After Model
                    "Before Model": "#66b3ff",  # สีฟ้าสำหรับ Before Model
                }.get(trace.name, "#9467bd")
            )
        )
    )  # ใช้สี default หากไม่พบ

    # ปรับ layout ของกราฟให้ดูโมเดิร์น
    fig.update_layout(
        plot_bgcolor="#f7f9fb",  # พื้นหลังกราฟ
        paper_bgcolor="#ffffff",  # พื้นหลังนอกกราฟ
        font=dict(size=14, color="#252525"),  # ฟอนต์
        title=dict(font=dict(size=20), x=0.5, xanchor="center"),  # ตั้งชื่อกราฟให้อยู่กลาง
        xaxis=dict(title="Time", showgrid=True, gridcolor="#e6e6e6", zeroline=False),
        yaxis=dict(
            title="Processing Time", showgrid=True, gridcolor="#e6e6e6", zeroline=False
        ),
        legend=dict(
            title="Model",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
        ),
    )

    return fig


@dash.callback(
    Output("plot-confidence", "figure"),
    Input("image-result-interval", "n_intervals"),
)
def update_confidence_plot(n_intervals):
    df1, df2 = load_and_process_data()

    confidence_data_before = process_confidence_data(df2, "Before")
    confidence_data_after = process_confidence_data(df1, "After")

    combined_data = pd.concat([confidence_data_after, confidence_data_before])

    fig = go.Figure()
    if len(combined_data) > 0:
        fig.add_trace(
            go.Violin(
                x=combined_data["label"][combined_data["label"] == "Before"],
                y=combined_data["confidence"][combined_data["label"] == "Before"],
                name="Before Model",
                box_visible=False,
                meanline_visible=True,
                points="all",
                jitter=0.1,
                marker=dict(opacity=0.4),
                line=dict(color="#ff9999"),
            )
        )
        fig.add_trace(
            go.Violin(
                x=combined_data["label"][combined_data["label"] == "After"],
                y=combined_data["confidence"][combined_data["label"] == "After"],
                name="After Model",
                box_visible=False,
                meanline_visible=True,
                points="all",
                jitter=0.05,
                marker=dict(opacity=0.3),
                line=dict(color="#66b3ff"),
            )
        )

        fig.add_trace(
            go.Box(
                x=combined_data["label"][combined_data["label"] == "Before"],
                y=combined_data["confidence"][combined_data["label"] == "Before"],
                name="Before model - Boxplot",
                boxmean=True,
                marker_color="#d30033",
                line_width=2,
                width=0.2,
            )
        )
        fig.add_trace(
            go.Box(
                x=combined_data["label"][combined_data["label"] == "After"],
                y=combined_data["confidence"][combined_data["label"] == "After"],
                name="After Model - Boxplot",
                boxmean=True,  # Show mean
                marker_color="rgb(0, 112, 153)",
                line_width=3,
                width=0.2,
            )
        )

        fig.update_layout(
            title_text="Normal Distribution with Box-Plot (Mean) for Confidence Values by Model",  # ชื่อกราฟ
            title_x=0.5,  # จัดให้ชื่อกราฟอยู่กลางห
            legend=dict(
                orientation="h",  # จัดแนวนอน
                yanchor="bottom",  # ยึดกับด้านล่าง
                xanchor="center",  # ยึดกับตรงกลาง
                x=0.5,  # อยู่ตรงกลางตามแกน x
                y=1.05,  # อยู่ใต้ชื่อกราฟ
            ),
            showlegend=True,  # แสดง legend
            plot_bgcolor="#f7f9fb",  # พื้นหลังกราฟ
            paper_bgcolor="#ffffff",  # พื้นหลังภายนอกกราฟ
            xaxis_title="Model",
            yaxis_title="Confidence",
            font=dict(size=14, color="#252525"),
            xaxis=dict(showgrid=True, gridcolor="#e6e6e6"),
            yaxis=dict(showgrid=True, gridcolor="#e6e6e6"),
            margin=dict(b=20, l=20, r=10),
        )

    return fig


@dash.callback(
    Output("bar-plot", "figure"),
    Input("image-result-interval", "n_intervals"),
)
def update_bar_chart(n_intervals):
    def extract_confidence(conf_list):
        if isinstance(conf_list, str) and conf_list:
            return max(eval(conf_list)) if eval(conf_list) else None
        return None

    # อ่านไฟล์ CSV
    df1, df2 = load_and_process_data()

    # ดึงค่าความเชื่อมั่นสูงสุด
    df1["confidence"] = df1["confidence"].apply(extract_confidence)
    df2["confidence"] = df2["confidence"].apply(extract_confidence)

    # กรองค่าที่ไม่เป็น NaN
    conf1 = df1["confidence"].dropna()
    conf2 = df2["confidence"].dropna()

    # ตั้งค่าช่วงของ bins
    bins = np.arange(0.4, 1.0, 0.1)

    # นับจำนวนค่าที่อยู่ในแต่ละช่วงสำหรับแต่ละ DataFrame
    hist1, _ = np.histogram(conf1, bins=bins)
    hist2, _ = np.histogram(conf2, bins=bins)

    # สร้างกราฟแท่ง
    fig = go.Figure()

    # แสดงแท่งสำหรับ SRResGan
    fig.add_trace(
        go.Bar(
            x=[f"{round(b, 1)} - {round(b + 0.1, 1)}" for b in bins[:-1]],
            y=hist1,
            name="SRResGan",
            marker_color="#ff9999",
        )
    )

    # แสดงแท่งสำหรับ NotGans โดยเลื่อนแท่งไปทางขวา
    fig.add_trace(
        go.Bar(
            x=[f"{round(b, 1)} - {round(b + 0.1, 1)}" for b in bins[:-1]],
            y=hist2,
            name="NotGans",
            marker_color="#66b3ff",
        )
    )

    # ตั้งค่าชื่อกราฟและแกน
    fig.update_layout(
        title="Distribution of Confidence Values for SRResGan and NotGans",
        xaxis_title="Confidence Ranges",
        yaxis_title="Frequency",
        legend=dict(x=0.1, y=1.0),
        template="simple_white",  # ใช้ธีมขาว
    )

    return fig
