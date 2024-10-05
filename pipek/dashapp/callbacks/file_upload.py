import os
import dash
import json
import base64
import datetime
import pathlib
import io
import time
from dash import html, dash_table
from PIL import Image

from flask import current_app

from pipek import models
from pipek.web import redis_rq
from pipek.jobs import face_detections
from tensorflow.keras.models import load_model
import numpy as np
import cv2


def bicubic_interpolate(image, shape):
    img_resized = cv2.resize(image, shape)
    # img_resized=cv2.resize(image,shape, interpolation=cv2.INTER_CUBIC)
    return img_resized


def model_predict(contents, filename, date):
    model_dir = "data/srgan_model"  # Directory where your model is stored
    model_path = os.path.join(model_dir, "SRResNet-generator01.h5")
    model = load_model(model_path)
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)

    image_dir_path = pathlib.Path(current_app.config.get("PIPEK_DATA")) / "images"

    image_object = io.BytesIO(decoded)
    im = Image.open(image_object)
    im_array = np.array(im)

    if im_array.shape[-1] == 4:
        im_array = im_array[..., :3]

    lr = bicubic_interpolate(im_array, (128, 128))
    pred_model = model.predict(np.array([lr]) / 255.0)
    pred_img_array = np.clip(pred_model[0] * 255, 0, 255).astype(np.uint8)
    pred_img = Image.fromarray(pred_img_array)

    stored_filename = f"{image_dir_path}/{filename}"
    stored_path = pathlib.Path(stored_filename)
    while stored_path.exists():
        stored_filename = f"{image_dir_path}/{round(time.time() * 1000)}-{filename}"
        stored_path = pathlib.Path(stored_filename)

    # with open(stored_filename, "wb") as f:
    #     f.write(pre_img.getbuffer())
    pred_img.save(stored_filename)

    image = models.Image(
        path=stored_filename,
        filename=filename,
    )

    models.db.session.add(image)
    models.db.session.commit()
    models.db.session.refresh(image)

    job = redis_rq.redis_queue.queue.enqueue(
        face_detections.detect,
        args=(image.id,),
        # job_id=f"",
        timeout=600,
        job_timeout=600,
    )

    return image.id, html.Div(f"{image.id} Upload Completed")


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)

    image_dir_path = (
        pathlib.Path(current_app.config.get("PIPEK_DATA")) / "images_original"
    )

    image_object = io.BytesIO(decoded)

    stored_filename = f"{image_dir_path}/{filename}"
    stored_path = pathlib.Path(stored_filename)
    while stored_path.exists():
        stored_filename = f"{image_dir_path}/{round(time.time() * 1000)}-{filename}"
        stored_path = pathlib.Path(stored_filename)

    with open(stored_filename, "wb") as f:
        f.write(image_object.getbuffer())

    image = models.ImageOriginal(
        path=stored_filename,
        filename=filename,
    )

    models.db.session.add(image)
    models.db.session.commit()
    models.db.session.refresh(image)

    job = redis_rq.redis_queue.queue.enqueue(
        face_detections.detect,
        args=(image.id,),
        # job_id=f"",
        timeout=600,
        job_timeout=600,
    )

    return image.id, html.Div(f"{image.id} Upload Completed")


@dash.callback(
    dash.Output("image-results", "children"),
    dash.Input("image-result-interval", "n_intervals"),
    dash.Input("image-ids", "data"),
)
def get_image_results(n_intervals, image_ids):
    if not image_ids:
        return "Not Upload"

    datas = json.loads(image_ids)
    re_size = 1280, 1280

    results = dict()
    for image_id in datas:
        image = models.db.session.get(models.Image, image_id)
        models.db.session.commit()

        results[image.id] = dict(status=image.status, updated_date=image.updated_date)

        image_results = image.path
        pil_image = Image.open(image_results)
        # pil_image.thumbnail(re_size, Image.Resampling.LANCZOS)

    return html.Div(
        html.Img(
            src=pil_image,
            style={
                "width": "auto",  # ให้รูปเต็มความกว้างของการ์ด
                "height": "auto",  # ปรับขนาดความสูงอัตโนมัติตามสัดส่วน
                "object-fit": "contain",
                "transform": "scale(2)",  # จัดการรูปภาพให้ไม่ล้นกรอบการ์ด
            },
        ),  # ปรับความสูงตามที่ต้องการ
    )


@dash.callback(
    dash.Output("upload-status", "children"),
    dash.Output("upload-image-ids", "children"),
    dash.Output("image-ids", "data"),
    dash.Input("upload-data", "contents"),
    dash.State("upload-data", "filename"),
    dash.State("upload-data", "last_modified"),
)
def upload_image(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is None:
        return "", "", ""

    children = []
    image_ids = []
    for c, n, d in zip(list_of_contents, list_of_names, list_of_dates):
        image_id, result = model_predict(c, n, d)
        children.append(result)
        image_ids.append(image_id)

    return children, html.Div(image_ids), json.dumps(image_ids)


# --------------------------- orginal ------------------------------------------ #


@dash.callback(
    dash.Output("image-original-results", "children"),
    dash.Input("image-original-result-interval", "n_intervals"),
    dash.Input("image-original-ids", "data"),
)
def get_original_image_results(n_intervals, image_ids):
    if not image_ids:
        return "Not Upload"

    datas = json.loads(image_ids)

    for image_id in datas:
        image = models.db.session.get(models.ImageOriginal, image_id)
        models.db.session.commit()

        image_results = image.path
        pil_image = Image.open(image_results)

    return html.Div(
        html.Img(
            src=pil_image,  # เปลี่ยน src ให้เป็น path ของรูปภาพ
            style={
                "width": "auto",  # ให้รูปเต็มความกว้างของการ์ด
                "height": "auto",  # ปรับขนาดความสูงอัตโนมัติตามสัดส่วน
                "object-fit": "contain",
                # "transform": "scale(2)",  # จัดการรูปภาพให้ไม่ล้นกรอบการ์ด
            },
        ),
        style={
            "width": "100%",  # ให้ div ครอบรูปเต็มการ์ด
        },
    )


@dash.callback(
    dash.Output("upload-original-status", "children"),
    dash.Output("upload-original-image-ids", "children"),
    dash.Output("image-original-ids", "data"),
    dash.Input("upload-data", "contents"),
    dash.State("upload-data", "filename"),
    dash.State("upload-data", "last_modified"),
)
def upload_original_image(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is None:
        return "", "", ""

    children = []
    image_ids = []
    for c, n, d in zip(list_of_contents, list_of_names, list_of_dates):
        image_id, result = parse_contents(c, n, d)
        children.append(result)
        image_ids.append(image_id)

    return children, html.Div(image_ids), json.dumps(image_ids)
