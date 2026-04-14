import joblib
import numpy as np

model = joblib.load("models/hidden_intent_model(org).pkl")
vectorizer = joblib.load("models/tfidf_vectorizer(org).pkl")


def predicr_intent(text, threshold=0.4):
    if not text or len(text.strip()) < 3:
        return {"error": "Input too short or empty"}

    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)

    prediction = {}
    for i, p in enumerate(probs):
        prediction[f"intent_{i}"] = int(p[0][1]>=threshold)
    return prediction