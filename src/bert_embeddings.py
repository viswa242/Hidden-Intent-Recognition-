import torch 
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

model.eval()

sentences = "Sure do whatever you want"

inputs = tokenizer(
    sentences,
    padding = True,
    truncation = True,
    max_length = 10,
    return_tensors = "pt"
)

with torch.no_grad():
    outputs = model(**inputs)

last_hidden_state = outputs.last_hidden_state

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

for token, embedding in zip(tokens, last_hidden_state[0]):
    print(f"{token}: {embedding[:5]}...")
cls_embedding = last_hidden_state[0][0]  # CLS token

print("CLS embedding shape:", cls_embedding.shape)
print("CLS embedding (first 5 values):", cls_embedding[:5])
print("\nSummary:")
print("Each token → contextual embedding")
print("CLS token → sentence-level meaning")
