import requests

def get_recommendations_from_ml_service(user_id, recent_products):
    url = "http://ml_service:8000/predict"

    response = requests.post(url, json={
        "user_id" : user_id, 
        "recent_products" : recent_products
    })
    
    if response.status_code==200:
        return response.json()["recommended_products"]
    else:
        return []
    
    