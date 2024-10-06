import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import io
import base64

# Initialize the Dash app
app = dash.Dash(__name__)

# # Layout ของหน้าเว็บ
# app.layout = html.Div([
#     dcc.Graph(id="graph", config={'displayModeBar': False}),
#     dcc.Graph(id="confidence-plot", config={'displayModeBar': False}),
#     dcc.Interval(id="interval-component", interval=1000, n_intervals=0),
#     html.Img(id="donut-chart", style={"width": "50%", "height": "50%"})
# ])

# Function to load and process data from CSV files
def load_and_process_data():
    file1 = "data/images/processing_results_af_gans.csv"
    file2 = "data/images/processing_results_bf_gans.csv"

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    return df1, df2

# Line graph callback (ใช้ Plotly แทน)
@app.callback(
    Output("graph", "figure"),
    Input("interval-component", "n_intervals")  # ใช้ interval ในการอัปเดต
)
def update_graph(n_intervals):
    df1, df2 = load_and_process_data()

    df1['processing_time_rolling'] = df1['processing_time'].rolling(window=10).mean()
    df2['processing_time_rolling'] = df2['processing_time'].rolling(window=10).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df1.index, y=df1['processing_time_rolling'],
        mode='lines+markers', name='SRResGan',
        line=dict(color='#ff9999')
    ))

    fig.add_trace(go.Scatter(
        x=df2.index, y=df2['processing_time_rolling'],
        mode='lines+markers', name='NotGans',
        line=dict(color='#66b3ff')
    ))

    fig.update_layout(
        title="Comparison of Rolling Mean Processing Time (Window=10)",
        xaxis_title="Index",
        yaxis_title="Rolling Mean of Processing Time",
        legend_title="Legend"
    )

    return fig

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
    Output("plot-confidence", "figure"),
    Input("interval-component", "n_intervals")  # ใช้ interval ในการอัปเดต
)
def update_confidence_plot(n_intervals):
    df1, df2 = load_and_process_data()

    confidence_data_after = process_confidence_data(df1, 'After')
    confidence_data_before = process_confidence_data(df2, 'Before')

    combined_data = pd.concat([confidence_data_after, confidence_data_before])
    fig = px.violin(x = None, y = None)
    if len(combined_data) > 0:
        fig = px.violin(combined_data, x='label', y='confidence', title='Violin Plot of Confidence Values (Before vs After)')
        fig.update_layout(xaxis_title='Data Source', yaxis_title='Confidence')
        print('##########################################################')
    return fig


    

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
