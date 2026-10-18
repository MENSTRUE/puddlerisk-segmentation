from pathlib import Path
from ultralytics import YOLO

ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_PATH = ROOT_DIR / "models" / "puddlerisk_v2_champion.pt"


def load_model(model_path: str | Path = DEFAULT_MODEL_PATH) -> YOLO:
    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model tidak ditemukan: {model_path}"
        )

    return YOLO(str(model_path))