# Disaster Tweet Analyzer

A web application that uses machine learning to analyze tweets and determine if they are about real disasters or not. The application features a modern, interactive UI with real-time analysis and beautiful visualizations.

## Features
- Real-time tweet analysis
- Modern, responsive UI with animations
- Circular confidence indicator
- Color-coded results for better visualization
- Machine learning-powered predictions

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Libraries**: scikit-learn, NLTK
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd disaster-tweet-analyzer
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Download required NLTK data:
```bash
python download_nltk_data.py
```

## Usage

1. Start the Flask application:
```bash
cd app
python app.py
```

2. Open your web browser and navigate to:
```
[http://localhost:5000](http://127.0.0.1:5000/)
```

3. Enter a tweet in the text area and click "Analyze Tweet" to get the prediction.

## Project Structure

```
.
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   │   └── index.html
│   └── app.py
├── data/
│   └── train.csv
├── model/
├── download_nltk_data.py
└── requirements.txt
```

## Model Training

The application uses a TF-IDF vectorizer and Logistic Regression model for classification. The model is automatically trained on first run using the data in `data/train.csv`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
