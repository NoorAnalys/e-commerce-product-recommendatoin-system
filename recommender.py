from __future__ import annotations
from pathlib import Path
from typing import List, Optional, Any
import joblib

MODEL_PATH = Path(__file__).resolve.parent / "model.joblib"

_model : Optional[Any] = None

def _load_model()-> Any:
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. "
                "Make sure you trained and saved model.joblib into ml_service/app/model/"
            )
        _model = joblib.load(MODEL_PATH)
        return _model
    
def get_recommendations(user_id : int, recent_products : List[int] , top_k : int = 10) -> List[int]:
    model = _load_model

    if hasattr (model, "recommend") and callable(model.recommend):
        return list(model.recommend(user_id = user_id, recent_products = recent_products, top_k = top_k))

    if isinstance(model, dict):
        recommend_fn = model.get("recommend")
        if callable(recommend_fn):
            return list(recommend_fn(user_id=user_id, recent_products=recent_products, top_k = top_k))
    
    raise TypeError(
        "Loaded model does not support recommendation yet. "
        "Expected a .recommend(...) method or a dict with a callable 'recommend'."
    )
