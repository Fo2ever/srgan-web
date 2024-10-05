import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ใช้ธีมสีขาว (Flatly)
app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

dash.register_page(__name__, path="/image-classify")


layout = html.Div(
    style={
        "backgroundColor": "white",
        "height": "100vh",
    },
    children=[
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Id",
                                    style={
                                        "text-align": "center",
                                        "color": "black",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            id="upload-image-ids",
                                            style={
                                                "text-align": "center",
                                                "color": "black",
                                            },
                                        ),
                                        html.Div(
                                            id="upload-original-image-ids",
                                            style={
                                                "text-align": "center",
                                                "color": "black",
                                            },
                                        ),
                                    ],
                                ),
                            ]
                        ),
                        style={
                            "height": "5rem",
                            "width": "6vw",
                            "backgroundColor": "#f5f5f5",
                            "borderRadius": "0.25rem",
                            "margin-left": "20px",
                            "margin-top": "10px",
                            "margin-right": "-8px",
                            "display": "none",
                        },
                    ),
                    width=2,
                ),
                dbc.Col(
                    dcc.Link(
                        html.Button(
                            html.H5(
                                "Next Pages",
                                style={
                                    "text-align": "left",
                                    "margin-top": "10px",
                                    "color": "black",
                                },
                            ),
                        ),  # Button styled as a link to Page 1
                        href="/dashboard/page_2",  # URL for Page 1
                    ),
                ),
                dbc.Col(
                    dcc.Link(
                        html.Button(
                            html.H5(
                                "Next Pages",
                                style={
                                    "text-align": "left",
                                    "margin-top": "10px",
                                    "color": "black",
                                },
                            ),
                        ),  # Button styled as a link to Page 1
                        href="/dashboard/image-classify",  # URL for Page 1
                    ),
                ),
            ],
            style={"justify-content": "space-between", "display": "flex"},
            className="mb-2 ",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                "Card 2",
                                html.Div(id="image-results", style={"color": "black"}),
                            ]
                        ),
                        style={
                            "height": "26rem",
                            "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
                            "borderRadius": "0.5rem",  # กำหนดความโค้งมน
                            "margin-left": "20px",
                            "margin-right": "-8px",  # ขยับจากขอบซ้าย
                        },
                    ),
                    width=4,  # Half width
                ),
            ],
            style={"margin-top": "10px", "justify-content": "center"},
        ),
        html.Button("Load Images", id="load-images-btn"),
        html.Div(id="image-choices"),
        html.Button("Submit", id="submit-btn", n_clicks=0),
        html.Div(id="classification-result-original"),
        html.Div(id="classification-result"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
