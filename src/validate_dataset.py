import pandas as pd

df = pd.read_csv(r"Data/Raw/hidden.csv")

print("Total Samples:", len(df))

print("\nLabel distribution:")
print(df.iloc[:, 1:].sum())

print("\nAny null values?")
print(df.isnull().sum())
