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
        "backgroundColor": "#F0F2F0",  # พื้นหลังสีขาวที่คุมทั้งหน้า
        "height": "100vh",
        "position": "relative",  # ทำให้ content ซ้อนทับกันได้
    },
    children=[
        # Page Header (อยู่เหนือพื้นหลังสีขาวแต่ใต้การ์ด)
        html.Div(
            [
                html.H1(
                    "SRGAN Model",
                    style={
                        "color": "white",
                        "marginBottom": "0",
                        "fontSize": "2.5rem",
                        "textAlign": "center",
                    },
                ),
                html.P(
                    "Original VS Super Resolution Images",
                    style={
                        "color": "white",
                        "marginTop": "0",
                        "fontSize": "1.2rem",
                        "textAlign": "center",
                    },
                ),
            ],
            style={
                # "background": "linear-gradient(to right, #000000, #5234ff)",  # สีเขียวสำหรับ header
                "background": "linear-gradient(to bottom, #373B44, #4286f4)",  # สีเขียวสำหรับ header
                "height": "16rem",  # กำหนดความสูงของ header
                "padding": "20px",
                "position": "absolute",  # ใช้ absolute เพื่อไม่ให้ดัน content ลงไป
                "top": "0",  # ตรึง header ที่ตำแหน่งบนสุด
                "width": "100%",
                "zIndex": "0",  # ให้อยู่เหนือพื้นหลังสีขาว
            },
        ),
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
                            "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
                            "borderRadius": "0.25rem",  # กำหนดความโค้งมน
                            # "padding-left": "10px",
                            "margin-left": "20px",
                            "margin-top": "10px",
                            "margin-right": "-8px",
                            "display": "none",
                            # เพิ่ม padding ด้านซ้าย
                        },
                    ),
                    width=2,  # 30% of the width
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
                                    "Classify",
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
                                href="/dashboard/image-classify",
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
            # style={"justify-content": "space-between", "display": "flex"},
            className="mb-2 ",
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        "Card 1",
                                        html.Div(
                                            id="image-original-results",
                                            style={
                                                "color": "black",
                                                "display": "flex",
                                                "justifyContent": "center",  # จัดกลางแนวนอน
                                                "alignItems": "center",
                                                "height": "100%",
                                            },
                                        ),
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
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        "Card 2",
                                        html.Div(
                                            id="image-results",
                                            style={
                                                "color": "black",
                                                "display": "flex",
                                                "justifyContent": "center",  # จัดกลางแนวนอน
                                                "alignItems": "center",  # จัดกลางแนวตั้ง
                                                "height": "100%",  # ให้ div สูงเต็มการ์ด เพื่อให้ alignItems ทำงานได้
                                            },
                                        ),
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
                    style={"margin-top": "60px", "justify-content": "center"},
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
                                                        [
                                                            "Drag and ",
                                                            html.A("Drop Your Pic"),
                                                        ],
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
                                                    "alignItems": "center",
                                                    # จัดกลางแนวตั้ง
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
                                                "padding": "10px",
                                                "margin-top": "15px",  # เพิ่ม padding ให้ข้อความ
                                            },
                                        ),
                                        html.Div(
                                            id="upload-status"
                                        ),  # เพิ่ม upload-status ที่นี่
                                        dcc.Interval(id="image-result-interval"),
                                        dcc.Store(id="image-ids"),
                                        html.Div(
                                            id="upload-original-status"
                                        ),  # เพิ่ม upload-status ที่นี่
                                        dcc.Interval(
                                            id="image-original-result-interval"
                                        ),
                                        dcc.Store(id="image-original-ids"),
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
                ),
            ]
        ),
        # 10px margin from Row 2
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
