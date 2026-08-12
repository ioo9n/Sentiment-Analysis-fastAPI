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
sentiment-analysis-api/
│
├── app.py                     # Main FastAPI application
├── sentiment_model.pkl        # Trained Machine Learning model
├── tfidf_vectorizer.pkl       # Saved TF-IDF Vectorizer
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

---

## ⚙️ Installation & Local Setup

Follow these steps to run the project locally on your machine:

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/sentiment-analysis-api.git
cd sentiment-analysis-api

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the FastAPI server:
uvicorn app:app --reload

4. Access the API locally:
- Open your browser and go to: http://127.0.0.1:8000
- Access the interactive Swagger UI documentation: http://127.0.0.1:8000/docs

---

## 🔌 API Endpoints

### 1. Home Endpoint (GET /)
- Description: Checks if the API is up and running.
- Response Example:
{
  "message": "Welcome to the Sentiment Analysis API! The model is running successfully."
}

### 2. Predict Sentiment (POST /predict)
- Description: Cleans input text, vectorizes it, and predicts whether the sentiment is Positive or Negative.
- Request Body (JSON):
{
  "tweet": "I am so happy with my project"
}
- Response Body (JSON):
{
  "original_tweet": "I am so happy with my project",
  "clean_tweet": "happy project",
  "sentiment": "Positive"
}

---


