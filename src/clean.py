import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()

df["clean_text"] = df["text"].apply(clean_text)