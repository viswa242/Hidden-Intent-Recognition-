from sklearn.feature_extraction.text import TfidfVectorizer
def create_vectorizer(max_features, ngram_range):
    return TfidfVectorizer(
        max_features = max_features,
        ngram_range = tuple(ngram_range)
    )