# 🚀 Sentiment Analysis API

A robust and lightweight RESTful API built with **FastAPI** for real-time sentiment analysis on text data (tweets). This project serves as the backend bridge, integrating a pre-trained Machine Learning model with production-ready endpoints.

---

## 🛠️ Tech Stack & Libraries
* **Python** (Core Language)
* **FastAPI** (Web Framework & Automatic Interactive Documentation)
* **Scikit-Learn / Joblib** (Model Serialization & Vectorization)
* **NLTK** (Natural Language Processing & Text Preprocessing)
* **Pandas / NumPy** (Data Manipulation)
* **Uvicorn** (ASGI Server)

---

## 📂 Project Structure
```text
sentiment-analysis-api/
│
├── twitter_sentiment_analysis_fsatapi
├── sentiment_model.pkl        # Trained Machine Learning model
├── tfidf_vectorizer.pkl       # Saved TF-IDF Vectorizer
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
