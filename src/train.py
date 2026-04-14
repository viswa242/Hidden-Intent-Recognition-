import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
df = pd.read_csv("Data/Processed/augmented_datasett.csv")
x = df["clean_text"]
y = df.drop(columns=["text", "clean_text"])
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range = (1,2)
)
x_vec = vectorizer.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(
    x_vec, y, test_size=0.2, random_state=42
)
model = MultiOutputClassifier(
    LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )
)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred, zero_division=0))
print(classification_report(y_test, y_pred))
joblib.dump(model,"models/hidden_intent_model(org).pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer(org).pkl")
report = classification_report(y_test, y_pred, output_dict=True)
pd.DataFrame(report).to_csv("results/day8_metrics.csv")
y_prob = model.predict_proba(x_test)
y_pred = np.array([
    (prob[:,1]>=0.3).astype(int)
    for prob in y_prob
]).T
print(classification_report(y_test, y_pred, zero_division=0))
