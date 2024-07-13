from flask import Flask, request
from PIL import Image
import io
import numpy as np
import os
from models.yolo import load_yolo_model
import base64
import json

app = Flask(__name__)

model = load_yolo_model()


@app.route("/classify_and_detect", methods=["PUT"])
def classify_and_detect():

    image_data = request.get_data()

    encoded_images = image_data.split(b",")
    results = []
    for encoded_img in encoded_images:

        imgdata = base64.b64decode(encoded_img)

        image = Image.open(io.BytesIO(imgdata))

        if image.mode != "RGB":
            image = image.convert("RGB")

        image_array = np.asarray(image)

        results = model.predict(image_array)

        detections = json.loads(results[0].tojson())

        names = [detection["name"] for detection in detections]

    return ",".join(names)


if __name__ == "__main__":
    app.run(host="192.168.100.142", debug=True)
