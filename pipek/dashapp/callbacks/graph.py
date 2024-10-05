import dash
from dash import dcc, html, Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button("Update Graph", id="update-graph-button", n_clicks=0),
    dcc.Graph(id="graph", config={'displayModeBar': False}),
    html.Button("Update Confidence Plot", id="update-confidence-button", n_clicks=0),
    dcc.Graph(id="confidence-plot", config={'displayModeBar': False}),
    dcc.Interval(id="interval-component", interval=1000, n_intervals=0),
    html.Img(id="donut-chart", style={"width": "50%", "height": "50%"})
])

# Function to load and process data from CSV files
def load_and_process_data():
    file1 = "data\images\processing_results_af_gans.csv"
    file2 = "data\images\processing_results_bf_gans.csv"

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    return df1, df2

# Line graph callback
@app.callback(
    Output("graph", "figure"),
    Input("update-graph-button", "n_clicks"),
)
def update_graph(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    df1, df2 = load_and_process_data()

    df1['processing_time_rolling'] = df1['processing_time'].rolling(window=10).mean()
    df2['processing_time_rolling'] = df2['processing_time'].rolling(window=10).mean()

    fig = plt.figure(figsize=(10, 6))
    plt.plot(df1['processing_time_rolling'], label='SRResGan', color='#ff9999', marker='o', linestyle='-')
    plt.plot(df2['processing_time_rolling'], label='NotGans', color='#66b3ff', marker='o', linestyle='-')

    plt.title('Comparison of Rolling Mean Processing Time (Window=10)')
    plt.xlabel('Index')
    plt.ylabel('Rolling Mean of Processing Time')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()

# Donut chart callback
@app.callback(
    Output("donut-chart", "src"),
    Input("interval-component", "n_intervals")
)
def update_donut_chart(n_intervals):
    df1, df2 = load_and_process_data()

    memory_size_file1 = df1['memory_size'].sum()
    memory_size_file2 = df2['memory_size'].sum()

    labels = ['SRResGan', 'NotGans']
    sizes = [memory_size_file1, memory_size_file2]

    colors = ['#ff9999', '#66b3ff']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.4})
    ax.axis('equal')  
    plt.title('Comparison of Memory Size from Two Files')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()

# Process confidence data function
def process_confidence_data(df, label):
    # Process confidence column
    df['confidence'] = df['confidence'].apply(lambda x: x.strip('[]') if isinstance(x, str) else x)
    df['confidence'] = pd.to_numeric(df['confidence'], errors='coerce')
    df = df[['confidence']].dropna()
    df['label'] = label
    return df

# Confidence plot callback
@app.callback(
    Output("confidence-plot", "figure"),
    Input("update-confidence-button", "n_clicks"),
)
def update_confidence_plot(n_clicks):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    df1, df2 = load_and_process_data()

    confidence_data_after = process_confidence_data(df1, 'After')
    confidence_data_before = process_confidence_data(df2, 'Before')

    combined_data = pd.concat([confidence_data_after, confidence_data_before])

    if len(combined_data) > 0:
        fig = sns.violinplot(x='label', y='confidence', data=combined_data).get_figure()
        fig.suptitle('Violin Plot of Confidence Values (Before vs After)')
        plt.xlabel('Data Source')
        plt.ylabel('Confidence')
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)
        return "data:image/png;base64," + base64.b64encode(img.getvalue()).decode()

    return None

