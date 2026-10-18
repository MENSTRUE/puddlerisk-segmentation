from pathlib import Path
import sys

import streamlit as st
from PIL import Image


ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from src.model import load_model
from src.inference import predict_puddle
from src.utils import (
    pil_to_bgr,
    bgr_to_rgb,
    format_confidence,
)


st.set_page_config(
    page_title="PuddleRisk",
    page_icon="💧",
    layout="wide",
)


@st.cache_resource
def get_model():
    return load_model()


model = get_model()


st.title("💧 PuddleRisk")

st.caption(
    "Puddle surface instance segmentation using YOLO11s-seg."
)


st.info(
    """
    PuddleRisk detects and segments visible puddle surfaces in road images.

    **Important:** mask coverage represents the percentage of image area
    predicted as puddle. It is **not** puddle depth, flood severity,
    hydroplaning probability, or physical road-risk score.
    """
)


uploaded_file = st.file_uploader(
    "Upload road image",
    type=["jpg", "jpeg", "png"],
)


with st.sidebar:
    st.header("Inference Settings")

    confidence = st.slider(
        "Confidence threshold",
        min_value=0.05,
        max_value=0.90,
        value=0.25,
        step=0.05,
    )

    iou = st.slider(
        "IoU threshold",
        min_value=0.10,
        max_value=0.90,
        value=0.60,
        step=0.05,
    )

    st.divider()

    st.markdown(
        """
        ### Model

        **YOLO11s-seg**

        Input size: **640 × 640**

        Champion:
        **PuddleRisk v2 Stage B**
        """
    )


if uploaded_file is None:
    st.write(
        "Upload an image to start segmentation."
    )

    st.stop()


image = Image.open(uploaded_file)

input_bgr = pil_to_bgr(image)


with st.spinner("Running segmentation..."):

    prediction = predict_puddle(
        model=model,
        image=input_bgr,
        conf=confidence,
        iou=iou,
        imgsz=640,
    )


output_rgb = bgr_to_rgb(
    prediction.annotated_image
)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    st.image(
        image,
        use_container_width=True,
    )

with col2:
    st.subheader("Prediction")
    st.image(
        output_rgb,
        use_container_width=True,
    )


st.divider()


m1, m2, m3 = st.columns(3)


with m1:
    st.metric(
        "Detected Puddle Instances",
        prediction.instance_count,
    )


with m2:
    st.metric(
        "Predicted Mask Coverage",
        f"{prediction.mask_coverage_pct:.2f}%",
    )


with m3:
    st.metric(
        "Mean Detection Confidence",
        format_confidence(
            prediction.confidences
        ),
    )


if prediction.instance_count == 0:

    st.warning(
        "No puddle instance was detected at the current confidence threshold."
    )

else:

    st.success(
        f"{prediction.instance_count} puddle instance(s) detected."
    )


with st.expander("Detection confidences"):

    if prediction.confidences:

        for index, confidence_value in enumerate(
            prediction.confidences,
            start=1,
        ):
            st.write(
                f"Instance {index}: "
                f"{confidence_value * 100:.2f}%"
            )

    else:
        st.write("No detections.")


st.divider()

st.caption(
    "PuddleRisk 10% Portfolio Project • "
    "Segmentation results are visual estimates only."
)