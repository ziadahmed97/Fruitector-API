from ultralytics import YOLO


def load_yolo_model():
    model = YOLO("best_float32 (3).tflite", task="detect")
    return model
