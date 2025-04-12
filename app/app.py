from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
import re
import joblib
import os

app = Flask(__name__)

# Download NLTK data
nltk.download('stopwords')

# Initialize the model and vectorizer
model = None
vectorizer = None

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove user @ references and '#' from tweet
    text = re.sub(r'\@\w+|\#', '', text)
    # Remove special characters and split into words
    words = re.findall(r'\w+', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def load_model():
    global model, vectorizer
    try:
        model = joblib.load('../model/disaster_model.pkl')
        vectorizer = joblib.load('../model/tfidf_vectorizer.pkl')
    except:
        # If model doesn't exist, train a new one
        train_model()

def train_model():
    global model, vectorizer
    # Load the training data
    train_data = pd.read_csv('../data/train.csv')
    
    # Preprocess the text
    train_data['processed_text'] = train_data['text'].apply(preprocess_text)
    
    # Create TF-IDF features
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(train_data['processed_text'])
    y = train_data['target']
    
    # Train the model
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    # Save the model and vectorizer
    os.makedirs('../model', exist_ok=True)
    joblib.dump(model, '../model/disaster_model.pkl')
    joblib.dump(vectorizer, '../model/tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.json['text']
        
        # Preprocess the text
        processed_text = preprocess_text(text)
        
        # Vectorize the text
        X = vectorizer.transform([processed_text])
        
        # Make prediction
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]
        
        return jsonify({
            'prediction': 'Disaster' if prediction == 1 else 'Not Disaster',
            'probability': float(probability)
        })

if __name__ == '__main__':
    load_model()
    app.run(debug=True) 