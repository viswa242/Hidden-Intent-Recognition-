import pandas as pd

df = pd.read_csv("data/raw/hidden_intent_dataset_v2.csv")

before = len(df)
df = df.drop_duplicates(subset=["text"])
after = len(df)

print(f"Before: {before}")
print(f"After removing duplicates: {after}")

df.to_csv("data/raw/hidden_intent_dataset_clean1.csv", index=False)
