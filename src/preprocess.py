import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "",text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    sample = "Sure, do whatever you want!!!"
    print("Original:", sample)
    print("Cleaned :", clean_text(sample))
