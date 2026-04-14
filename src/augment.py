import pandas as pd
import re
import nltk
import nlpaug.augmenter.word as naw
df = pd.read_csv(r"Data\Raw\hidden.csv")
label_cols = df.columns[1:]
print("label distribution: \n")
for col in label_cols:
    print(f"{col}: {df[col].sum()}")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()

df["clean_text"] = df["text"].apply(clean_text)

aug = naw.SynonymAug(aug_src = 'wordnet')
def augment_text(text, n=2):
    if len(text.split()) < 4:
        return []
    return aug.augment(text, n=n)
augmented_rows = []

for _, row in df.iterrows():
    if row[label_cols].sum() >0:
        augmented_texts = augment_text(row["clean_text"])
        for aug_text in augmented_texts:
            new_row = row.copy()
            new_row["clean_text"] = aug_text
            augmented_rows.append(new_row)
aug_df = pd.DataFrame(augmented_rows)
final_df = pd.concat([df, aug_df], ignore_index=True)
final_df.to_csv("Data/Processed/augmented_datasett.csv", index=False)

print("Augmentation completed!")
print("Original size:", len(df))
print("Augmented size", len(final_df))