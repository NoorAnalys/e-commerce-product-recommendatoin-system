from fastapi import FastAPI
from .schemas import PredictionRequest, PredictionResponse
from .utils import load_model, get_product_recommendations
import os
import numpy as np


model = load_model('app/model/model.joblib')
product_features = np.load('app/model/product_features.npy')  # Ensure you have this file ready

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    recommended_products = get_product_recommendations(
        request.user_id, request.recent_products, model, product_features
    )
    return PredictionResponse(recommended_products=recommended_products)
