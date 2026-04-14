from src.inference.predict_with_confidence import predict_with_confidence

class SingleSentenceMode:
    def process(self, engine, text: str):
        # No memory, no session
        result = predict_with_confidence(text)
        return {
            "mode": "single",
            "result": result
        }