from src.inference.predict_with_confidence import predict_with_confidence


class AdvancedConversationMode:
    def process(self, engine, session_id: str, text: str):
        # Session-based, memory ON
        result = predict_with_confidence(text)
        engine.add_message(result["final_intent"])

        summary = engine.get_summary()

        return {
            "mode": "advanced",
            "result": result,
            "summary": summary
        }