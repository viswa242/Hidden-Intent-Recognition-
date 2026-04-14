import pandas as pd
from preprocess import clean_text

df = pd.read_csv(r"Data\Raw\sampletext.csv")

df["clean_text"] = df["text"].apply(clean_text)
print(df)
