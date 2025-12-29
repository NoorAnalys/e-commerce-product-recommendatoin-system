import joblib 

model = joblib.load("model.joblib")

def get_recommendations(user_id, recent_products):
    recommendations = model.predict(recent_products)

    return recommendations
