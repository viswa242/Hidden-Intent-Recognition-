import joblib
import numpy as np
model = joblib.load("models/hidden_intent_model(org).pkl")
vectorizer = joblib.load("models/tfidf_vectorizer(org).pkl")

INTENT_LABELS = [
    "passive_aggression",
    "indirect_disagreement",
    "stress_masking",
    "avoidance",
    "manipulative_agreement",
    "genuine_agreement",
    "fake_politeness",
    "neutral"
]



HIGH_THRESHOLD = 0.4
LOW_THRESHOLD = 0.25
def predict_intent(text):
    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)
    results = {
        "high_confidence": [],
        "possible_intents": [],
        "neutral": False
    }
    for i, p in enumerate(probs):
        score = p[0][1]
        if score >= HIGH_THRESHOLD:
            results["high_confidence"].append(
                (INTENT_LABELS[i], round(score,3))
            )
        elif score >= LOW_THRESHOLD:
            results["possible_intents"].append(
                (INTENT_LABELS[i], round(score, 3))

            )
    if not results["high_confidence"] and not results["possible_intents"]:
        results["neutral"] = True
    return results
