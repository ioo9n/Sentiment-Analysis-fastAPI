from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

vectorizer = joblib.load('tfidf_vectorizer-2.pkl')
model = joblib.load('sentiment_model.pkl')

app = FastAPI(title="Sentiment Analysis API", version="1.0")

class TweetRequest(BaseModel):
    tweet: str

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z]', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running successfully!"}

@app.post("/predict")
def predict_sentiment(request: TweetRequest):
    cleaned = clean_text(request.tweet)
    vectorized_text = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized_text)[0]
    
    sentiment = "Positive" if prediction == 4 else "Negative"

    return {
        "original_tweet": request.tweet,
        "clean_tweet": cleaned,
        "sentiment": sentiment
    }
