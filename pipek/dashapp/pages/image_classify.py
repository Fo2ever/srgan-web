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
                dbc.Row(
                    dbc.Col(
                        [
                            dcc.Link(
                                html.Button(
                                    "Summary",
                                    style={
                                        "background-color": "#000000",  # Black background
                                        "color": "#FFFFFF",  # White text
                                        "border": "none",  # No border
                                        "border-radius": "50px",  # Rounded corners for pill shape
                                        "padding": "10px 20px",  # Padding to adjust size
                                        "font-size": "16px",  # Default font size
                                        "cursor": "pointer",  # Pointer on hover
                                        "text-align": "center",  # Center text
                                        "margin-right": "20px",  # Margin between buttons
                                    },
                                ),
                                href="/dashboard/page_2",
                            ),
                            dcc.Link(
                                html.Button(
                                    "Upload-Image",
                                    style={
                                        "background-color": "#000000",  # Black background
                                        "color": "#FFFFFF",  # White text
                                        "border": "none",  # No border
                                        "border-radius": "50px",  # Rounded corners
                                        "padding": "10px 20px",  # Padding to adjust size
                                        "font-size": "16px",  # Default font size
                                        "cursor": "pointer",  # Pointer on hover
                                        "text-align": "center",  # Center text
                                    },
                                ),
                                href="/dashboard/image-dashboard",
                            ),
                        ],
                        style={
                            "display": "flex",  # Flexbox for row layout
                            "justify-content": "center",  # Center items horizontally
                            "align-items": "center",  # Center items vertically
                            "margin-top": "10px",
                            "margin-left": "80rem",
                            "position": "relative",  # ให้ปุ่มอยู่ในตำแหน่ง relative เพื่อใช้ z-index ได้
                            "zIndex": "15",
                        },
                    ),
                ),
            ],
            style={"justify-content": "space-between", "display": "flex"},
            className="mb-2 ",
        ),
        html.Div(
            html.Button(
                "Load Images (Name)",
                id="load-images-btn",
                style={
                    "background-color": "#000000",  # Black background
                    "color": "#FFFFFF",  # White text
                    "border": "none",  # No border
                    "border-radius": "50px",  # Rounded corners for pill shape
                    "padding": "10px 20px",  # Padding to adjust size
                    "font-size": "16px",  # Default font size
                    "cursor": "pointer",  # Pointer on hover
                    "text-align": "center",  # Center text
                    "margin-left": "20px",  # Margin between buttons
                },
            ),
            style={
                "display": "flex",  # Flexbox for row layout
                "justify-content": "center",  # Center horizontally
                "align-items": "center",  # Center vertically (optional)
                "height": "5vh",  # Full viewport height to vertically center
            },
        ),
        html.Div(
            id="image-choices",
            style={
                "display": "flex",  # Flexbox layout
                "color": "#FFFFFF",
                "flex-direction": "column",  # Stack button and dropdown vertically
                "align-items": "center",  # Center horizontally
                "margin-top": "50px",  # Space from top of the screen
            },
        ),
        html.Button("Submit", id="submit-btn", n_clicks=0),
        html.Div(id="classification-result"),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
