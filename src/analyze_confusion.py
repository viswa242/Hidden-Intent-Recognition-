import pandas as pd
import joblib
import numpy as np

model = joblib.load("models/hidden_intent_model(org).pkl")
vectorizer = joblib.load("models/tfidf_vectorizer(org).pkl")

df = pd.read_csv("Data/Processed/augmented_datasett.csv")
X = vectorizer.transform(df["clean_text"])
y_true = df.drop(columns=["text", "clean_text"])

y_pred = model.predict(X)

confusion_cases = []
for i in range(len(y_true)):
    true_labels = y_true.iloc[i]
    pred_labels = y_pred[i]

    if not np.array_equal(true_labels.values, pred_labels):
        confusion_cases.append({
            "text": df.iloc[i]["clean_text"],
            "true": true_labels[true_labels==1].index.tolist(),
            "predicted": y_true.columns[pred_labels==1].tolist()
        })
conf_df = pd.DataFrame(confusion_cases)
conf_df.to_csv("results/confusion_cases.csv", index= False)
print(f"Confusion cases saved: {len(conf_df)}")
