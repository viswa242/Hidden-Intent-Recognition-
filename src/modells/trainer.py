from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(X, y, vectorizer, config):
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y,
        test_size=config["model"]["test_size"],
        random_state=config["model"]["random_state"]
    )
    model = MultiOutputClassifier(
        LogisticRegression(max_iter=config["model"]["max_iter"])
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "models/hidden_intent_model(org).pkl")
    joblib.dump(vectorizer, "models/tfidf_vectrizer(org).pkl")
    return model, X_test, y_test