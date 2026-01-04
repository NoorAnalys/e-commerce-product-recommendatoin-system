from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    user_id : int
    recent_products : List[int]

class PredictionResponse(BaseModel):
    recommended_products : List[int]