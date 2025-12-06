import streamlit as st
import joblib
import re
import string


# 1. Load the Saved Artifacts (Model & Vectorizer)
# We use @st.cache_resource to load them only once, making the app faster.
@st.cache_resource
def load_artifacts():
    model = joblib.load('nlp_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    return model, vectorizer


try:
    model, vectorizer = load_artifacts()
    print("✅ Model and Vectorizer loaded successfully!")
except FileNotFoundError:
    st.error("❌ Error: Model files not found. Please run the notebook first.")
    st.stop()


# 2. Define the Preprocessing Function (The "Cleaner")
# We must apply EXACTLY the same cleaning rules as in training.
def clean_text_for_app(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # No URLs
    text = re.sub(r'\@\w+|\#', '', text)  # No mentions
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # No numbers/punctuation
    return text


# 3. Build the User Interface (Frontend)
st.set_page_config(page_title="Disaster Tweet Detector", page_icon="🚨")

st.title("🚨 Disaster Tweet Classifier")
st.markdown("""
This AI model analyzes text to detect if it's a **Real Disaster** or just **Metaphorical/Fake**.
*Built with NLP (TF-IDF + Logistic Regression).*
""")

# Input box for the user
user_input = st.text_area("Enter a tweet or sentence here:", height=100,
                          placeholder="E.g.: There is a huge fire in the forest!")

# 4. Prediction Logic
if st.button("Analyze Tweet 🔍"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # A. Clean the input
        cleaned_text = clean_text_for_app(user_input)

        # B. Vectorize (Text -> Numbers)
        # Note: We use .transform(), NEVER .fit_transform() here!
        vectorized_text = vectorizer.transform([cleaned_text])

        # C. Predict
        prediction = model.predict(vectorized_text)[0]
        probability = model.predict_proba(vectorized_text)[0][1]  # Probability of being '1' (Disaster)

        # D. Display Result
        st.divider()
        if prediction == 1:
            st.error(f"🚨 ALERT: This looks like a REAL DISASTER! (Confidence: {probability:.1%})")
        else:
            st.success(f"✅ SAFE: This seems like a normal tweet. (Confidence: {1 - probability:.1%})")