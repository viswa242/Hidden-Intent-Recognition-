import pandas as pd
def load_dataset(path, text_column):
    df = pd.read_csv(path)
    X = df[text_column]
    y = df.drop(columns=["text", text_column])
    return X, y