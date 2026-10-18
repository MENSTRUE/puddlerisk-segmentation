import cv2
import numpy as np
from PIL import Image


def pil_to_bgr(image: Image.Image) -> np.ndarray:
    rgb = np.array(image.convert("RGB"))

    return cv2.cvtColor(
        rgb,
        cv2.COLOR_RGB2BGR,
    )


def bgr_to_rgb(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB,
    )


def format_confidence(values: list[float]) -> str:
    if not values:
        return "No detections"

    avg = sum(values) / len(values)

    return f"{avg * 100:.1f}%"