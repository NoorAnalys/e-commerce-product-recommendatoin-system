# 🛍️ E-Commerce Backend API (FastAPI + MySQL) + 🤖 AI Recommendation System 🚀

This repository contains **two main parts**:

1) **Backend API** (FastAPI + MySQL) — core e-commerce services  
2) **AI Recommendation System** — ML notebooks + an ML microservice (deployable via Docker)

They are developed **in parallel** by the team and integrated through clear API/service boundaries. 🤝

---

## 📦 Repository Structure (Backend + AI)

```bash
.
├── app/                          # 🛒 Backend API (FastAPI + MySQL)
│   ├── api/
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── user.py
│   │       ├── address.py
│   │       ├── category.py
│   │       ├── product.py
│   │       ├── cart.py
│   │       ├── order.py
│   │       ├── payment.py
│   │       ├── coupon.py
│   │       ├── review.py
│   │       ├── interaction.py
│   │       └── recommendation.py          #🤖 Backend endpoints that call AI service
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── logging.py
│   │   └── permissions.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── user.py
│   │   ├── address.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── product_image.py
│   │   ├── product_variant.py
│   │   ├── inventory.py
│   │   ├── cart/
│   │   │   ├── cart.py
│   │   │   └── cart_item.py
│   │   ├── order/
│   │   │   ├── order.py
│   │   │   └── order_item.py
│   │   ├── payment.py
│   │   ├── coupon.py
│   │   ├── review.py
│   │   └── interaction.py
│   ├── schemas/
│   │   ├── common.py
│   │   ├── token.py
│   │   ├── user.py
│   │   ├── address.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   ├── coupon.py
│   │   ├── review.py
│   │   └── interaction.py
│   ├── services/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── inventory.py
│   │   ├── payment.py
│   │   ├── interaction.py
│   │   ├── recommendation_client.py       # 🌐 calls ML service
│   │   └── recommendation_service.py      # 🧩 orchestration + fallback
│   └── main.py
│
├── data/                         # 📁 AI datasets (raw/processed) / sample data
├── docs/                         # 📄 documentation
├── ml_notebooks/                 # 📓 AI experiments & training notebooks
│   ├── 01_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_train_recommender.ipynb
│
├── ml_service/                   # 🤖 ML Microservice (Dockerized)
│   ├── app/                      # FastAPI inference service (implementation inside)
│   ├── Dockerfile
│   └── requirements.txt
│
├── scripts/                      # 🛠️ helper scripts
│   └── make_sample_data.py
│
├── docker-compose.yml            # 🐳 compose (backend + mysql + ml service if used)
├── .gitignore
├── LICENSE
└── README.md
```

## 🧠 What Each Part Does

### 🛒 Backend (FastAPI + MySQL)

- Handles all business logic: users, products, cart, orders, payments, coupons, reviews, interactions  
- Stores interaction data needed for recommendations (views / likes / favorites / orders)  
- Exposes recommendation endpoints that call the ML service (or fallback logic if ML is unavailable)

---

### 🤖 AI Recommendation System

**Two layers:**

- **Notebooks (`ml_notebooks/`)**  
  Data exploration → feature engineering → model training  

- **ML Service (`ml_service/`)**  
  An inference API that serves recommendation results to the backend

---

## 🤝 Integration (Backend ↔ ML Service)

- Backend calls the ML Service via HTTP using  
  `app/services/recommendation_client.py`
- Orchestration and fallback logic handled in  
  `app/services/recommendation_service.py`
- Public endpoints exposed in  
  `app/api/routes/recommendation.py`

### 🔄 Typical Flow

1. User interacts with products → backend stores interaction data  
2. AI team trains the model (notebooks) and exports model artifacts  
   (optionally to `data/` or a model registry)  
3. `ml_service` loads the trained model and serves `/recommendations`  
4. Backend queries the ML service and returns results to the frontend

---

## 🔧 Run Backend (API)


pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000



# 📌 Status

Backend API: 🚀 Implementing

MySQL integration: 🚀 Implementing

AI notebooks (exploration → training): 🤖🚀 Implementing

ML inference service: 🤖🚀 Implementing

Full integration testing: ⏳ In progress
