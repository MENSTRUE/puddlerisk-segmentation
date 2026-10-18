from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO


@dataclass
class PuddlePrediction:
    annotated_image: np.ndarray
    instance_count: int
    mask_coverage_pct: float
    confidences: list[float]


def predict_puddle(
    model: YOLO,
    image,
    conf: float = 0.25,
    iou: float = 0.60,
    imgsz: int = 640,
) -> PuddlePrediction:

    results = model.predict(
        source=image,
        imgsz=imgsz,
        conf=conf,
        iou=iou,
        retina_masks=True,
        verbose=False,
    )

    result = results[0]

    annotated = result.plot()

    instance_count = 0
    coverage_pct = 0.0
    confidences: list[float] = []

    if result.boxes is not None and len(result.boxes) > 0:
        instance_count = len(result.boxes)

        if result.boxes.conf is not None:
            confidences = (
                result.boxes.conf
                .detach()
                .cpu()
                .numpy()
                .astype(float)
                .tolist()
            )

    if (
        result.masks is not None
        and result.masks.data is not None
        and len(result.masks.data) > 0
    ):
        masks = (
            result.masks.data
            .detach()
            .cpu()
            .numpy()
            > 0.5
        )

        union_mask = np.any(masks, axis=0)

        coverage_pct = float(
            union_mask.mean() * 100.0
        )

    return PuddlePrediction(
        annotated_image=annotated,
        instance_count=instance_count,
        mask_coverage_pct=coverage_pct,
        confidences=confidences,
    )