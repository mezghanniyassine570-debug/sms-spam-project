import streamlit as st
import pickle
import re
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Try to load NLTK stopwords; fall back to a small built-in set if unavailable.
try:
    from nltk.corpus import stopwords
    try:
        STOPWORDS = set(stopwords.words('english'))
    except LookupError:
        STOPWORDS = None
except Exception:
    STOPWORDS = None

if not STOPWORDS:
    STOPWORDS = {
        'a','an','the','and','or','but','if','in','on','at','of','for','to','is','are','was','were',
        'be','been','being','have','has','had','do','does','did','not','no','so','than','that',
        'this','these','those','with','as','by','from','it','its','i','you','he','she','we','they',
        'me','him','her','us','them','my','your','his','her','our','their','what','which','who',
        'whom','whose','when','where','why','how','all','any','both','each','few','more','most',
        'other','some','such','only','own','same','too','very','can','will','just'
    }


def transform_text(text):
    """Lightweight text preprocessing without relying on NLTK data downloads.

    - lowercases
    - extracts word tokens with regex
    - removes stopwords
    - applies Porter stemming
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    # Tokenize on word characters (equivalent to simple word_tokenize)
    tokens = re.findall(r"\b\w+\b", text)
    # Filter stopwords
    tokens = [t for t in tokens if t not in STOPWORDS]
    # Stem
    tokens = [ps.stem(t) for t in tokens]
    return " ".join(tokens)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")