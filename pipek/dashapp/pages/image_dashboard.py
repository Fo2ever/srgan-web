import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ใช้ธีมสีขาว (Flatly)
app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

dash.register_page(__name__, path="/image-dashboard")

image_result_interval = dcc.Interval(
    id="image-result-interval",
    interval=1000,  # in milliseconds
    n_intervals=0,
)

layout = html.Div(
    style={
        # "backgroundColor": "white",
        "height": "100vh",
        "backgroundImage": "url(C:\ProjectEcoFinal\srgan-web\ct.jpg)",  # แทนที่ด้วย path ของภาพของคุณ
        "backgroundSize": "cover",  # ปรับขนาดภาพให้เต็มพื้นหลัง
        "backgroundPosition": "center",
        "opacity": "0.25",
    },  # ตั้งค่าพื้นหลังเป็นสีขาว
    children=[
        # Row 1 - Two Cards (images_id and images_detail)
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
                                    id="upload-image-ids",
                                    style={"text-align": "center", "color": "black"},
                                ),
                            ]
                        ),
                        style={
                            "height": "5rem",
                            "width": "6vw",
                            "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
                            "borderRadius": "0.25rem",  # กำหนดความโค้งมน
                            # "padding-left": "10px",
                            "margin-left": "20px",
                            "margin-top": "10px",
                            "margin-right": "-8px",
                            # เพิ่ม padding ด้านซ้าย
                        },
                    ),
                    width=2,  # 30% of the width
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Next Pages",
                                    style={
                                        "text-align": "left",
                                        "margin-top": "10px",
                                        "color": "black",
                                    },
                                ),
                                # html.Div(id="image-results", style={"color": "black"}),
                            ]
                        ),
                        style={
                            "height": "5rem",
                            "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
                            "borderRadius": "0.5rem",
                            "display": "flex",  # ใช้ Flexbox
                            "justify-Content": "flex-end",  # จัดกลางแนวนอน
                            "alignItems": "center",  # จัดกลางแนวตั้ง
                            "margin-right": "20px",
                            "margin-top": "10px",
                            "margin-left": "-8px",  # กำหนดความโค้งมน
                        },
                    ),
                    width=2,  # 20% of the width
                ),
            ],
            style={"justify-content": "space-between", "display": "flex"},
            className="mb-2 ",
        ),  # Adds margin-bottom for spacing between rows
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody("Card 1"),
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
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody("Card 2"),
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
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Upload(
                                    id="upload-data",
                                    children=html.Div(
                                        [
                                            html.Div(
                                                ["Drag and ", html.A("Drop Your Pic")],
                                                style={"color": "#0d3b31"},
                                            ),
                                            html.Div(
                                                html.I(
                                                    id="hover-target",
                                                    className="fa fa-upload fa-3x",
                                                    style={"opacity": "0.25"},
                                                ),  # ใช้ไอคอน fa-upload
                                                style={
                                                    "marginTop": "10px",
                                                    "color": "#145b4c",
                                                },  # ขยับไอคอนลงมาจากข้อความ
                                            ),
                                        ],
                                        style={
                                            "color": "black",
                                            "display": "flex",  # ใช้ Flexbox
                                            "flexDirection": "column",  # จัดแนวในแนวตั้ง
                                            "justifyContent": "center",  # จัดกลางแนวนอน
                                            "alignItems": "center",  # จัดกลางแนวตั้ง
                                        },
                                    ),
                                    style={
                                        "height": "7rem",
                                        "backgroundColor": "#f5f5f5",
                                        "borderRadius": "0.5rem",
                                        "display": "flex",  # ใช้ Flexbox
                                        "justify-content": "center",  # จัดกลางแนวนอน
                                        "alignItems": "center",  # จัดกลางแนวตั้ง
                                        "margin-top": "2rem",
                                    },
                                    multiple=True,
                                ),
                                dbc.Popover(
                                    "Upload Here",  # ข้อความที่จะแสดงใน Popover
                                    target="hover-target",  # target คือไอคอนที่มี id = hover-target
                                    body=True,
                                    trigger="hover",
                                    placement="bottom",  # ให้แสดงที่ด้านล่างของไอคอน
                                    style={
                                        "backgroundColor": "#145b4c",  # พื้นหลังสีขาว
                                        "color": "#f5f5f5",  # สีตัวอักษร #252525
                                        "borderRadius": "0.5rem",  # ปรับความโค้งของ popover
                                        "padding": "10px",  # เพิ่ม padding ให้ข้อความ
                                    },
                                ),
                                html.Div(id="upload-status"),  # เพิ่ม upload-status ที่นี่
                                dcc.Interval(id="image-result-interval"),
                                dcc.Store(id="image-ids"),
                            ]
                        ),
                        style={
                            "height": "14rem",
                            "backgroundColor": "#f5f5f5",
                            "borderRadius": "0.5rem",  # กำหนดความโค้งมน
                            "margin-left": "20px",
                            "margin-right": "-8px",
                            "margin-top": "6rem",
                        },
                    ),
                    width=3,  # Half width
                ),
            ],
            style={"justify-content": "center"},
        ),  # 10px margin from Row 2
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)


# layout = html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.Card(
#                         dbc.CardBody(
#                             [
#                                 html.H5(
#                                     "Image Ids",
#                                     style={
#                                         "text-align": "left",
#                                         "margin": 0,
#                                         "color": "black",
#                                     },
#                                 ),
#                                 html.Div(
#                                     id="upload-image-ids", style={"color": "black"}
#                                 ),
#                             ],
#                         ),
#                         style={
#                             "height": "6rem",  # เพิ่มความสูงเป็น 6rem
#                             "background-color": "white",
#                             "border-radius": "0.25rem",
#                         },
#                     ),
#                     width=3,  # 30% of the row
#                 ),
#                 dbc.Col(
#                     dbc.Card(
#                         dbc.CardBody(
#                             [
#                                 html.H5(
#                                     "Image Results",
#                                     style={
#                                         "text-align": "left",
#                                         "margin": 0,
#                                         "color": "black",
#                                     },
#                                 ),
#                                 html.Div(id="image-results", style={"color": "black"}),
#                             ],
#                         ),
#                         style={
#                             "height": "6rem",  # เพิ่มความสูงเป็น 6rem
#                             "background-color": "white",
#                             "border-radius": "0.25rem",
#                         },
#                     ),
#                     width=7,  # 70% of the row
#                 ),
#             ],
#             style={"margin-bottom": "10px"},  # margin-bottom for the Row
#         ),
#         dcc.Upload(
#             id="upload-data",
#             children=html.Div(
#                 ["Drag and Drop or ", html.A("Select Files")], style={"color": "black"}
#             ),
#             style={
#                 "width": "100%",
#                 "height": "60px",
#                 "lineHeight": "60px",
#                 "borderWidth": "1px",
#                 "borderStyle": "dashed",
#                 "borderRadius": "5px",
#                 "textAlign": "center",
#                 "margin": "10px",
#                 "background-color": "white",
#             },
#             multiple=True,
#         ),
#         html.Div(
#             id="upload-status", style={"color": "black", "background-color": "white"}
#         ),
#         image_result_interval,
#         dcc.Store(id="image-ids"),
#     ],
#     style={"background-color": "white"},  # Set background of the entire page to white
# )
