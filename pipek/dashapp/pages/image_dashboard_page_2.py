import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# ใช้ธีมสีขาว (Flatly)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__, path="/page_2")

image_result_interval = dcc.Interval(
    id="image-result-interval",
    interval=1000,  # in milliseconds
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
        "backgroundColor": "#edf2f7ff",
        # "width": "100vw",
        "height": "120vh",
        # "padding": "0",
        # "margin": "0",
        # "box-sizing": "border-box",
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
                                        "ENHANCE CT_SCAN PICTURE DASHBOARD",
                                        style={
                                            "color": "#252525",
                                            "padding-top": "10px",
                                            "text-align": "center",  # Center the text horizontally
                                            "margin": "0",
                                            "margin-left": "20px",  # Remove default margins
                                        },
                                    ),
                                    html.Div(
                                        [
                                            dcc.Link(
                                                html.Button(
                                                    "Upload-Image",
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
                                                href="/dashboard/image-dashboard",
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
                                    "test",
                                    body=True,
                                    style={
                                        "height": "10rem",
                                        "margin-bottom": "15px",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-left": "30px solid #4169e1",  # Blue left border
                                        "border-radius": "10px",  # Rounded corners for the card
                                    },
                                ),
                                dbc.Card(
                                    body=True,
                                    style={
                                        "height": "18rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "border-left": "30px solid #a020f0",  # Blue left border
                                        "border-radius": "10px",  # Rounded corners for the card
                                    },
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
                                        "border-bottom": "10px solid black",  # Blue left border
                                        "border-radius": "10px",
                                    },
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
                                        "border-right": "5px solid #ffc40c",  # Blue left border
                                        "border-radius": "10px",
                                    },
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
                                        "height": "22rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                    },
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
                                        "height": "22rem",
                                        "backgroundColor": "#ffffff",  # Set card background color to white
                                        "box-shadow": "rgba(33, 40, 50, 0.15) 0px 2.4px 28px 0px",
                                        "box-radius": "0.35rem",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ],
)


# layout = html.Div(
#     style={"backgroundColor": "white", "height": "100vh"},  # ตั้งค่าพื้นหลังเป็นสีขาว
#     children=[
# Row 1 - Two Cards (images_id and images_detail)
# dbc.Row(
#     [
#         dbc.Col(
#             dbc.Card(
#                 dbc.CardBody(
#                     [
#                         html.H5(
#                             "Previous Page",
#                             style={
#                                 "text-align": "center",
#                                 "margin": 0,
#                                 "color": "black",
#                                 "margin-top": "10px",
#                             },
#                         ),
#                         html.Div(
#                             id="upload-image-ids",
#                             style={"text-align": "center", "color": "black"},
#                         ),
#                     ]
#                 ),
#                 style={
#                     "height": "5rem",
#                     "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
#                     "borderRadius": "0.25rem",  # กำหนดความโค้งมน
#                     "padding-left": "10px",
#                     "display": "flex",  # ใช้ Flexbox
#                     "justifyContent": "center",  # จัดกลางแนวนอน
#                     "alignItems": "center",
#                     "margin-left": "20px",
#                     "margin-top": "10px",
#                     "margin-right": "-20px",
#                     # เพิ่ม padding ด้านซ้าย
#                 },
#             ),
#             width=2,  # 30% of the width
#         ),
#         # dbc.Col(
#         #     dbc.Card(
#         #         dbc.CardBody(
#         #             [
#         #                 html.H5(
#         #                     "Image Results",
#         #                     style={
#         #                         "text-align": "left",
#         #                         "margin": 0,
#         #                         "color": "black",
#         #                     },
#         #                 ),
#         #             ]
#         #         ),
#         #         style={
#         #             "height": "5rem",
#         #             "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
#         #             "borderRadius": "0.25rem",
#         #             "margin-top": "10px",
#         #             "margin-left": "-8px",
#         #             "margin-right": "10px",
#         #         },
#         #     ),
#         #     width=2,  # 70% of the width
#         # ),
#     ],
#     className="mb-2",
# ),  # Adds margin-bottom for spacing between rows
# # Row 2 - Full Width Card
# dbc.Col(
#     dbc.Card(
#         dbc.CardBody(
#             [
#                 dcc.Upload(
#                     id="upload-data",
#                     children=html.Div(
#                         [
#                             html.Div(
#                                 ["Drag and ", html.A("Drop Your Pic")],
#                                 style={"color": "#0d3b31"},
#                             ),
#                             html.Div(
#                                 html.I(
#                                     id="hover-target",
#                                     className="fa fa-upload fa-2x",
#                                     style={"opacity": "0.35"},
#                                 ),  # ใช้ไอคอน fa-upload
#                                 style={
#                                     "marginTop": "10px",
#                                     "color": "#145b4c",
#                                 },  # ขยับไอคอนลงมาจากข้อความ
#                             ),
#                         ],
#                         style={
#                             "color": "black",
#                             "display": "flex",  # ใช้ Flexbox
#                             "flexDirection": "column",  # จัดแนวในแนวตั้ง
#                             "justifyContent": "center",  # จัดกลางแนวนอน
#                             "alignItems": "center",  # จัดกลางแนวตั้ง
#                         },
#                     ),
#                     style={
#                         "height": "7rem",
#                         "backgroundColor": "#f5f5f5",
#                         "borderRadius": "0.5rem",
#                         "display": "flex",  # ใช้ Flexbox
#                         "justify-content": "center",  # จัดกลางแนวนอน
#                         "alignItems": "center",  # จัดกลางแนวตั้ง
#                         # "margin-top": "2rem",
#                     },
#                     multiple=True,
#                 ),
#                 dbc.Popover(
#                     "Upload Here",  # ข้อความที่จะแสดงใน Popover
#                     target="hover-target",  # target คือไอคอนที่มี id = hover-target
#                     body=True,
#                     trigger="hover",
#                     placement="bottom",  # ให้แสดงที่ด้านล่างของไอคอน
#                     style={
#                         "backgroundColor": "#145b4c",  # พื้นหลังสีขาว
#                         "color": "#f5f5f5",  # สีตัวอักษร #252525
#                         "borderRadius": "0.5rem",  # ปรับความโค้งของ popover
#                         "padding": "10px",  # เพิ่ม padding ให้ข้อความ
#                     },
#                 ),
#                 html.Div(id="upload-status"),  # เพิ่ม upload-status ที่นี่
#                 dcc.Interval(id="image-result-interval"),
#                 dcc.Store(id="image-ids"),  # Corrected Store ID
#             ]
#         ),
#         style={
#             "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
#             "borderRadius": "0.25rem",  # กำหนดความโค้งมน
#             "border-bottom": "4px solid",  # กำหนดความหนาและสไตล์ของเส้น
#             "border-bottom-color": "#145b4c",
#             "margin-left": "20px",
#             "margin-bottom": "10px",
#             # เพิ่ม padding ด้านซ้าย
#         },
#     ),
#     width=2,
# ),
# dbc.Col(
#     [
#         # การ์ดใบที่ 1
#         dbc.Card(
#             dbc.CardBody(
#                 [
#                     dcc.Upload(
#                         id="Accuracy-OG",
#                         children=html.Div(
#                             [
#                                 html.Div(
#                                     ["Original"],
#                                     style={"color": "#0d3b31"},
#                                 ),
#                             ],
#                             style={
#                                 "color": "black",
#                                 "display": "flex",  # ใช้ Flexbox
#                                 "flexDirection": "column",  # จัดแนวในแนวตั้ง
#                                 "justifyContent": "center",  # จัดกลางแนวนอน
#                                 "alignItems": "center",  # จัดกลางแนวตั้ง
#                             },
#                         ),
#                         style={
#                             "height": "4rem",
#                             "backgroundColor": "#f5f5f5",
#                             "borderRadius": "0.5rem",
#                             "display": "flex",  # ใช้ Flexbox
#                             "justify-content": "center",  # จัดกลางแนวนอน
#                             "alignItems": "center",  # จัดกลางแนวตั้ง
#                         },
#                     ),
#                 ]
#             ),
#             style={
#                 "backgroundColor": "#f5f5f5",  # เปลี่ยนสีพื้นหลังการ์ด
#                 "borderRadius": "0.25rem",  # กำหนดความโค้งมน
#                 "border-bottom": "4px solid",  # กำหนดความหนาและสไตล์ของเส้น
#                 "border-bottom-color": "#FF0000",
#                 "margin-left": "20px",
#                 "margin-bottom": "10px",  # เพิ่มระยะห่างระหว่างการ์ดสองใบ
#             },
#         ),
#         # การ์ดใบที่ 2
#         dbc.Card(
#             dbc.CardBody("Card 2 Content"),
#             style={
#                 "height": "6rem",
#                 "backgroundColor": "#f5f5f5",  # พื้นหลังการ์ด
#                 "borderRadius": "0.25rem",  # ความโค้งของมุมการ์ด
#                 "border-bottom": "4px solid",  # เส้นขอบล่าง
#                 "border-bottom-color": "#FFCC00",
#                 "margin-left": "20px",  # สีของเส้นขอบล่าง
#                 "margin-bottom": "10px",  # เพิ่มระยะห่างระหว่างการ์ดสองใบ
#             },
#         ),
#     ],
#     width=2,
# ),
# # 10px margin from Row 1
# # Row 3 - Two Cards (half-width, height 15 rem)  # 10px margin from Row 2
#     ],
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)


# layout = html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         html.H2(["Image Ids"]),
#                         html.Div(id="upload-image-ids"),
#                     ]
#                 ),
#                 dbc.Col(
#                     [
#                         html.H2(["Image Results"]),
#                         html.Div(id="image-results"),
#                     ]
#                 ),
#             ]
#         ),
#         dcc.Upload(
#             id="upload-data",
#             children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
#             style={
#                 "width": "100%",
#                 "height": "60px",
#                 "lineHeight": "60px",
#                 "borderWidth": "1px",
#                 "borderStyle": "dashed",
#                 "borderRadius": "5px",
#                 "textAlign": "center",
#                 "margin": "10px",
#             },
#             # Allow multiple files to be uploaded
#             multiple=True,
#         ),
#         html.Div(id="upload-status"),
#         image_result_interval,
#         dcc.Store(id="image-ids"),
#     ]
# )
