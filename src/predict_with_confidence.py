from inference.predictor import predict_intent

INTENT_GROUPS = {
    "agreement_related": [
        "genuine_agreement",
        "manipulative_agreement",
        "fake_politeness"
    ],
    "disagreement_related": [
        "indirect_disagreement",
        "passive_aggression"
    ],
    "avoidance_related": [
        "avoidance",
        "stress_masking"
    ],
    "neutral": [
        "neutral"
    ]
}

def confidence_level(score):
    if score >= 0.6:
        return "High"
    elif score >= 0.3:
        return "Medium"
    elif score >= 0.15:
        return "Low"
    else:
        return "Very Low"


def predict_with_confidence(text):
    base_result = predict_intent(text)

    enriched_possible = []
    group_scores = {}

    for intent, score in base_result["possible_intents"]:
        enriched_possible.append({
            "intent": intent,
            "score": score,
            "confidence": confidence_level(score)
        })

        for group, intents in INTENT_GROUPS.items():
            if intent in intents:
                group_scores[group] = group_scores.get(group, 0) + score

    dominant_group = (
        max(group_scores, key=group_scores.get)
        if group_scores else "neutral"
    )

    return {
        "high_confidence": base_result["high_confidence"],
        "possible_intents": enriched_possible,
        "intent_group": dominant_group,
        "neutral": base_result["neutral"]
    }
