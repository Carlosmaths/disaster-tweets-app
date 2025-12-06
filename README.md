# 🚨 Disaster Tweets Classifier

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-ff4b4b.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![NLP](https://img.shields.io/badge/Technique-NLP%20%2F%20TF--IDF-purple.svg)

## 🚀 Live Demo
**[🔗 Access the App Here](INSERT_YOUR_STREAMLIT_LINK_HERE)**

---

## 📖 Project Overview

This application uses **Natural Language Processing (NLP)** to automatically classify tweets into two categories:
1.  **Real Disasters** (e.g., "Fire in the building", "Earthquake").
2.  **Non-Disasters** (e.g., Metaphorical uses like "This song is fire").

The goal is to help emergency organizations (like 911 or Red Cross) filter noise from social media during crises to improve response times.

### 🎯 Key Features
* **Real-time Prediction:** Users can input any text to get an immediate classification.
* **Confidence Score:** The model provides a probability percentage for its decision.
* **Text Preprocessing:** Includes automated Regex cleaning and Stopwords removal.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn (Logistic Regression)
* **Vectorization:** TF-IDF (Term Frequency - Inverse Document Frequency)
* **Serialization:** Joblib

---

## 📊 Model Performance

The model was trained on a dataset of ~7,600 tweets.

* **Algorithm:** Logistic Regression (Solver: liblinear)
* **Vectorization:** TF-IDF (Top 5,000 features)
* **Accuracy:** ~80% on Test Data
* **Key Insight:** The model successfully distinguishes between semantic contexts, achieving a balance between precision and recall suitable for a first-pass filter.

---

## 📂 Repository Structure

```text
├── app.py                   # Streamlit Application (Frontend & Logic)
├── nlp_model.pkl            # Trained Logistic Regression Model
├── tfidf_vectorizer.pkl     # Fitted TF-IDF Vectorizer (Vocabulary)
├── requirements.txt         # Project Dependencies
├── .gitignore               # Ignored files configuration
└── README.md                # Documentation

💻 Local Installation
To run this project on your local machine:

Clone the repository:
Bash:

git clone [https://github.com/Carlosmaths/disaster-tweets-app.git](https://github.com/Carlosmaths/disaster-tweets-app.git)
cd disaster-tweets-app

Install dependencies:
Bash:

pip install -r requirements.txt

Run the application:
Bash

streamlit run app.py

Author:
Carlos Barrios: Mathematician | University Professor | Data Scientist

LinkedIn: https://www.linkedin.com/in/carlos-barrios-matematicas-fisica-machinelearning/
GitHub: https://github.com/Carlosmaths
