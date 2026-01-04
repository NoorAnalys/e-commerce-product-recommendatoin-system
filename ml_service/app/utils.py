import joblib
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from typing import List

def load_model(model_path : str):
    return joblib.load(model_path)

def get_product_recommendations(user_id : int, recent_products : List[int], model, product_features : np.ndarray )-> List[int]:
    similarity_scores = cosine_similarity(product_features[recent_products],product_features)

    avg_scores = np.mean(similarity_scores,axis=0)

    recommend_indices = np.argsort(avg_scores)[::-1]

    return recommend_indices.tolist()