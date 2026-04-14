from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
sentences = [
    "sure do whatever you want",
    "im fine no issue at all"
]

encoded = tokenizer(
    sentences,
    padding = True,
    truncation = True,
    max_length = 10,
    return_tensors = "pt"
)
print(encoded)

