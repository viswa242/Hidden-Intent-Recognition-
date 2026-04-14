# def process_input(user_input, mode="advanced"):
#     if mode == "single":
#         prediction = predict_with_confidence(user_input)
#         return {
#             "mode": "single_sentence",
#             "prediction": prediction
#         }
#     elif mode == "advanced":
#         prediction = predict_with_confidence(user_input)
    
#         conversation_engine.add_message(prediction["final_intent"])
#         state = conversation_engine.get_state()  # or get_summary()

#         return {
#             "mode": "advanced_conversation",
#             "prediction": prediction,
#             "conversation_state": state
#         }

# from src.speech.speech_to_text import recognize_speech
from src.inference.predict_with_confidence import predict_with_confidence
from src.conversation_engine import ConversationEngine
conversation_engine = ConversationEngine()
def process_input(user_input, mode="advanced"):
    """
    mode:
        - "single" → Single sentence hidden intent
        - "advanced" → Full conversation intelligence
    """

    # Run prediction first
    prediction = predict_with_confidence(user_input)

    # -----------------------------
    # MODE 1 → Single Sentence
    # -----------------------------
    
    result = process_input(user_input, mode=selected_mode)
    print(result)
    if mode == "single":
        return {
            "mode": "single_sentence",
            "prediction": prediction
        }

    # -----------------------------
    # MODE 2 → Advanced Conversation
    # -----------------------------
    elif mode == "advanced":

        # Update conversation memory
        conversation_engine.add_message(prediction["final_intent"])

        # Get updated state
        conversation_state = conversation_engine.get_summary()

        return {
            "mode": "advanced_conversation",
            "prediction": prediction,
            "conversation_state": conversation_state
        }

    else:
        return {
            "error": "Invalid mode selected. Choose 'single' or 'advanced'."
        }
print("Select Mode:")
print("1 - Single Sentence Hidden Intent")
print("2 - Advanced Conversation Intelligence")

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    selected_mode = "single"
else:
    selected_mode = "advanced"

