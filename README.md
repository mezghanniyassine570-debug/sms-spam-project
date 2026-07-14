# SMS Spam Classifier

A simple spam detection web app built with Streamlit, using a trained text preprocessing pipeline and a Naive Bayes classifier.

## What it does

- Loads an SMS dataset
- Cleans and stems text
- Converts text to TF-IDF vectors
- Classifies messages as spam or not spam
- Serves the model through a Streamlit app (`app.py`)

## Files in this repo

- `app.py` — Streamlit application entrypoint
- `model.pkl` — serialized trained model
- `vectorizer.pkl` — serialized TF-IDF vectorizer
- `spam.csv` — original dataset used for training
- `README.md` — project documentation

## How to run locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate
   ```
2. Install dependencies:
   ```bash
   pip install streamlit scikit-learn pandas numpy nltk wordcloud
   ```
3. Start the app:
   ```bash
   streamlit run app.py
   ```

## Notes for deployment

- This app is ready for deployment on Hugging Face Spaces or Streamlit Community Cloud.
- Keep `model.pkl` and `vectorizer.pkl` in the repo so the app can load them.
- If using Hugging Face Spaces, add a `requirements.txt` file with the same dependencies.



## Author

Built as a lightweight SMS spam classification demo with a shareable web UI.
