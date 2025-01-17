import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ใช้ธีมสีขาว (Flatly)
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,  # ใช้ธีม Bootstrap
        "https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap",  # ใช้ฟอนต์ Nunito จาก Google Fonts
    ],
)
dash.register_page(__name__, path="/page_2")

image_result_interval = dcc.Interval(
    id="image-result-interval",
    interval=1000000,  # in milliseconds
    n_intervals=0,
)
STYLE_OG_ACC = {"width": "100%", "height": "4rem", "margin-bottom": "2vh"}

Accuracy_OG = dbc.Card(
    dbc.CardBody(
        [
            html.P("Original Accuracy", className="card-text text-center"),
        ]
    ),
    style=STYLE_OG_ACC,
)

import dash_bootstrap_components as dbc
from dash import html

import dash_bootstrap_components as dbc
from dash import html

layout = html.Div(
    style={
        # "backgroundColor": "#e6ecf2ff",
        # "backgroundColor": "rgb(232, 245, 255)",
        # "backgroundColor": "rgb(232, 245, 255)",
        "backgroundColor": "rgb(230, 243, 255)",
        # "backgroundColor": "#edf2f7ff",
        # "width": "100vw",
        "height": "120vh",
        # "padding": "0",
        # "margin": "0",
        # "box-sizing": "border-box",
        "font-family": "Nunito, sans-serif",
    },
    children=[
        html.Div(
            children=[
                html.Div(
                    [
                        dbc.Row(
                            dbc.Col(
                                [
                                    html.H2(
                                        "ENHANCE MRI BRAIN TUMOR IMAGE DASHBOARD",
                                        style={
                                            "color": "#252525",
                                            "padding-top": "10px",
                                            "text-align": "center",  # Center the text horizontally
                                            "margin": "0",
                                            "margin-left": "20px",
                                            # "fontFamily": "'Roboto', sans-serif",  # Remove default margins
                                            "fontFamily": "Nunito, sans-serif",
                                        },
                                    ),
                                    html.Div(
                                        [
                                            dcc.Link(
                                                html.Button(
                                                    "Upload-Image",
                                                    style={
                                                        "background-color": "rgb(250, 109, 87)",  # Black background
                                                        # "background-color": "#000000",  # Black background
                                                        "color": "#FFFFFF",  # White text
                                                        "border": "none",  # No border
                                                        "border-radius": "50px",  # Rounded corners for pill shape
                                                        "padding": "10px 20px",  # Padding to adjust size
                                                        "font-size": "16px",  # Default font size
                                                        "cursor": "pointer",  # Pointer on hover
                                                        "text-align": "center",  # Center text
                                                        "margin-right": "20px",  # Margin between buttons
                                                        # "fontFamily": "'Roboto', sans-serif",
                                                    },
                                                ),
                                                href="/dashboard/image-dashboard",
                                            ),
                                            dcc.Link(
                                                html.Button(
                                                    "Classify",
                                                    style={
                                                        "background-color": "#4169e1",  # Black background
                                                        "color": "#FFFFFF",  # White text
                                                        "border": "none",  # No border
                                                        "border-radius": "50px",  # Rounded corners
                                                        "padding": "10px 20px",  # Padding to adjust size
                                                        "font-size": "16px",  # Default font size
                                                        "cursor": "pointer",  # Pointer on hover
                                                        "text-align": "center",
                                                        "margin-right": "20px",  # Center text
                                                    },
                                                ),
                                                href="/dashboard/image-classify",
                                            ),
                                        ],
                                        style={
                                            "display": "flex",  # Flexbox for row layout
                                            "justify-content": "flex-end",  # Align buttons to the right
                                            "align-items": "center",  # Center items vertically
                                            "margin-left": "auto",  # Push buttons to the right
                                        },
                                    ),
                                ],
                                style={
                                    "display": "flex",  # Flexbox for row layout
                                    "justify-content": "space-between",  # Space between h2 and buttons
                                    "align-items": "center",
                                    "padding-top": "20px",  # Align items vertically in center
                                },
                            )
                        )
                    ]
                ),
                # Row 1
                html.Div(
                    style={
                        "display": "flex",
                        "margin-bottom": "20px",
                        "margin-top": "20px",
                    },
                    children=[
                        # Column 1 with two cards
                        html.Div(
                            style={
                                "width": "calc(100% * 3 / 12)",
                                "margin-left": "20px",
                            },
                            children=[
                                dbc.Card(
                                    "MODEL : SRGANs",
                                    body=True,
                                    style={
                                        "color": "#252525",
                                        "margin-bottom": "15px",
                                        "margin-top": "5px",
                                        "height": "5rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-left": "10px solid rgb(0, 160, 168)",  # Blue left border
                                        "border-radius": "10px",  # Rounded corners for the card
                                        "textAlign": "center",  # จัดข้อความให้อยู่กลาง
                                        "fontSize": "34px",  # ขยายขนาดข้อความ
                                        "fontWeight": "bold",  # ทำให้ข้อความเป็นตัวหนา
                                    },
                                ),
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "23rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-left": "10px solid rgb(255, 182, 46)",  # Blue left border
                                        "border-radius": "10px",  # Rounded corners for the card
                                    },
                                    children=[
                                        dcc.Graph(
                                            id="donut-chart",
                                            style={
                                                "width": "100%",
                                                "height": "100%",
                                            },  # ปรับให้เต็มพื้นที่
                                            config={
                                                "displayModeBar": False
                                            },  # ลบแถบเครื่องมือของกราฟ
                                        ),
                                        dcc.Interval(id="image-result-interval"),
                                    ],
                                ),
                            ],
                        ),
                        # Column 2 with one card
                        html.Div(
                            style={
                                "width": "calc(100% * 6.5 / 12)",
                                "margin-left": "20px",
                            },
                            children=[
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "29rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-bottom": "10px solid rgb(79, 111, 214)",  # Blue left border  # Blue left border
                                        # "border-bottom": "10px solid #4169e1",  # Blue left border  # Blue left border
                                        "border-radius": "10px",
                                    },
                                    children=[
                                        dcc.Graph(
                                            id="plot-confidence",
                                            style={
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                            # ใส่กราฟในนี้
                                            config={"displayModeBar": False},
                                        ),
                                        dcc.Interval(id="image-result-interval"),
                                    ],
                                ),
                            ],
                        ),
                        # Column 3 with one card
                        html.Div(
                            style={
                                "width": "calc(100% * 2 / 12)",
                                "margin-left": "20px",
                            },
                            children=[
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "29rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-right": "10px solid rgb(255, 182, 46)",  # Yellow right border
                                        "border-radius": "10px",
                                        "display": "flex",  # ใช้ flexbox เพื่อจัดให้อยู่ตรงกลาง
                                        "justify-content": "center",  # จัดแนวนอนให้อยู่ตรงกลาง
                                        "align-items": "center",  # จัดแนวตั้งให้อยู่ตรงกลาง
                                    },
                                    children=[
                                        html.Div(
                                            [
                                                html.Span(
                                                    "Sample data for comparison between images without the model and images processed by the SRGAN model, with a total of",
                                                    style={
                                                        "textAlign": "center",
                                                        "fontSize": "20px",  # ขนาดของข้อความส่วนแรก
                                                        "color": "#252525",
                                                        "marginTop": "40px",  # สีข้อความส่วนแรก
                                                        "display": "inline-block",  # เปลี่ยน display เพื่อให้ margin ทำงาน
                                                    },
                                                ),
                                                html.Span(
                                                    "371 Images",  # ข้อความที่แยกออกมา
                                                    style={
                                                        "textAlign": "center",
                                                        "fontSize": "36px",  # ขยายขนาดฟอนต์สองเท่า
                                                        "color": "#ffcc00",  # สีเหลือง
                                                        "fontWeight": "bold",  # ข้อความเป็นตัวหนา
                                                        "marginTop": "45px",  # ระยะห่างระหว่างประโยคแรก
                                                        "display": "block",  # จัดให้อยู่คนละบรรทัด
                                                    },
                                                ),
                                            ],
                                            style={
                                                "textAlign": "center"
                                            },  # จัดข้อความทั้งหมดให้อยู่ตรงกลาง
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                # Row 2
                html.Div(
                    style={"display": "flex"},
                    children=[
                        # First card in second row
                        html.Div(
                            style={
                                "width": "calc(100% * 6 / 12)",
                                "margin-left": "20px",
                            },
                            children=[
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "29rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-left": "10px solid rgb(250, 109, 87)",  # Blue left border
                                        "border-radius": "10px",
                                    },
                                    children=[
                                        dcc.Graph(
                                            id="time-process-chart",
                                            style={
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                        dcc.Interval(id="image-result-interval"),
                                    ],
                                ),
                            ],
                        ),
                        # Second card in second row
                        html.Div(
                            style={
                                "width": "47vw",
                                "margin-left": "12px",
                                # "margin-right": "16px",
                            },
                            children=[
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "29rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-right": "10px solid rgb(0, 112, 153)",  # Blue left border
                                        "border-radius": "10px",
                                    },
                                    children=[
                                        dcc.Graph(
                                            id="bar-plot",
                                            style={
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                        dcc.Interval(id="image-result-interval"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ],
)
