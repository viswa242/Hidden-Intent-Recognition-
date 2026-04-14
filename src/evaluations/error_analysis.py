import pandas as pd
import joblib
from sklearn.metrics import classification_report
model = joblib.load("models/hidden_intent_model(org).pkl")
vectorizer = joblib.load("models/tfidf_vectorizer(org).pkl")
df = pd.read_csv("Data/Processed/augmented_datasett.csv")
X = vectorizer.transform(df["clean_text"])
y_true = df.drop(columns=["text", "clean_text"])

y_pred = model.predict(X)

y_pred_df = pd.DataFrame(y_pred, columns=y_true.columns)

errors = df.copy()
errors["mismatch_count"] = (y_true != y_pred_df).sum(axis=1)

error_cases = errors[errors["mismatch_count"]>0]
error_cases.to_csv("results/day10_error_cases.csv", index=False)

print(f"Total error cases:{len(error_cases)}")