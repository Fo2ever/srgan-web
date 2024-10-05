import os
import dash
import json
import base64
import datetime
import pathlib
import io
import time
from dash import html, dash_table, dcc
from PIL import Image, ImageDraw

from flask import current_app

from pipek import models
from pipek.web import redis_rq
from pipek.jobs import face_detections
from tensorflow.keras.models import load_model
from inference_sdk import InferenceHTTPClient
import numpy as np
import cv2

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="sMTNsFHnYQSgqOitGmnk",  # ใช้ API Key ของคุณเอง
)


@dash.callback(
    dash.Output("image-choices", "children"),
    dash.Input("load-images-btn", "n_clicks"),
)
def get_image_results(n_clicks):
    if n_clicks is None:
        return dash.no_update

    images = models.db.session.query(models.Image).all()
    models.db.session.commit()

    dropdown_options = [
        {"label": image.filename, "value": image.id} for image in images
    ]
    first_image_id = images[0].id

    return html.Div(
        [
            dcc.Dropdown(
                id="image-dropdown",
                options=dropdown_options,
                placeholder="Select an image",
                value=first_image_id,
                clearable=False,
                style={
                    "width": "15rem",  # Adjust width of the dropdown
                    "margin-top": "20px",  # Space between button and dropdown
                    "background-color": "#f0f0f0",  # Light background color for dropdown
                    "border-radius": "10px",  # Rounded corners for dropdown
                    "font-size": "16px",  # Font size
                    # "padding": "10px",  # Padding for the dropdown content
                    "color": "#252525",  # Change text color to white
                },
            )
        ]
    )


@dash.callback(
    dash.Output("classification-result", "children"),
    dash.Input("submit-btn", "n_clicks"),
    dash.Input("image-dropdown", "value"),
)
def get_image_results(n_clicks, selected_image_id):
    if n_clicks is None:
        return "Please select an image first"

    image_srgan = models.db.session.get(models.Image, selected_image_id)
    image_original = models.db.session.get(models.ImageOriginal, selected_image_id)

    models.db.session.commit()
    image_path = image_srgan.path
    image_original_path = image_original.path

    if image_path.lower().endswith((".jpg", ".jpeg", ".png")):

        image = Image.open(image_path)
        classify_model = client.infer(image_path, model_id="axial-mri/1")
        draw = ImageDraw.Draw(image)
        predictions = classify_model["predictions"]

        for pred in predictions:

            x_center = pred["x"]
            y_center = pred["y"]
            width = pred["width"]
            height = pred["height"]

            left = x_center - width / 2
            top = y_center - height / 2
            right = x_center + width / 2
            bottom = y_center + height / 2

            draw.rectangle([left, top, right, bottom], outline="red", width=3)

            confidence = pred["confidence"]
            draw.text((left, top - 10), f"Confidence: {confidence:.2f}", fill="yellow")

            has_tumor = True

        image = image.convert("RGB")

    if image_original_path.lower().endswith((".jpg", ".jpeg", ".png")):

        image_original = Image.open(image_original_path)
        classify_model = client.infer(image_original_path, model_id="axial-mri/1")
        draw_original = ImageDraw.Draw(image_original)
        predictions = classify_model["predictions"]

        for pred in predictions:

            x_center = pred["x"]
            y_center = pred["y"]
            width = pred["width"]
            height = pred["height"]

            left = x_center - width / 2
            top = y_center - height / 2
            right = x_center + width / 2
            bottom = y_center + height / 2

            draw_original.rectangle([left, top, right, bottom], outline="red", width=3)

            confidence = pred["confidence"]
            draw_original.text(
                (left, top - 10), f"Confidence: {confidence:.2f}", fill="yellow"
            )

            has_tumor = True

        image_original = image_original.convert("RGB")
        image_original = image_original.resize((440, 440), Image.LANCZOS)

    # นำภาพเข้า model classify
    return html.Div(
        [
            html.Div(
                html.Img(src=image_original),
                style={
                    "margin-right": "20px",  # เพิ่มระยะห่างระหว่างรูปภาพ
                },
            ),
            html.Div(html.Img(src=image)),
        ],
        style={
            "display": "flex",  # Use flexbox to manage layout
            "flex-direction": "row",  # Stack images horizontally
            "align-items": "center",  # Center images vertically
            "margin-top": "20px",  # Space between dropdown and images
            "justify-content": "center",  # Center images horizontally
        },
    )
