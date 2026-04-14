# from src.inference.predictor import predict_intent

# INTENT_GROUPS = {
#     "agreement_related": [
#         "genuine_agreement",
#         "manipulative_agreement",
#         "fake_politeness"
#     ],
#     "disagreement_related": [
#         "indirect_disagreement",
#         "passive_aggression"
#     ],
#     "avoidance_related": [
#         "avoidance",
#         "stress_masking"
#     ],
#     "neutral": [
#         "neutral"
#     ]
# }
# INTENT_PRIORITY = [
#     "passive_aggression",
#     "manipulative_agreement",
#     "indirect_disagreement",
#     "fake_politeness",
#     "stress_masking",
#     "avoidance",
#     "genuine_agreement",
#     "neutral"
# ]


# def confidence_level(score):
#     if score >= 0.6:
#         return "High"
#     elif score >= 0.3:
#         return "Medium"
#     elif score >= 0.15:
#         return "Low"
#     else:
#         return "Very Low"


# def predict_with_confidence(text):
#     base_result = predict_intent(text)

#     enriched_possible = []
#     group_scores = {}

#     for intent, score in base_result["possible_intents"]:
#         enriched_possible.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })

#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     dominant_group = (
#         max(group_scores, key=group_scores.get)
#         if group_scores else "neutral"
#     )

#     return {
#         "high_confidence": base_result["high_confidence"],
#         "possible_intents": enriched_possible,
#         "intent_group": dominant_group,
#         "neutral": base_result["neutral"]
#     }
# def decide_final_intent(results):
#     all_intents = results["high_confidence"] + results["possible_intents"]
#     if not all_intents:
#         return "neutral"
#     for intent in INTENT_PRIORITY:
#         for item in all_intents:
#             if item["intent"] == intent:
#                 return intent
#     return "neutral"

# def generate_explanation(final_intent, results):
#     if final_intent == "neutral":
#         return "The text does not strongly indicate any hidden or indirect intent."
#     return f"The text shows linguistic patterns associated with '{final_intent}', such as indirect phrasing or controlled agreement."

# final_intent = decide_final_intent(results)
# explanation = generate_explanation(final_intent, results)
# return {
#     "final_intent": final_intent,
#     "intent_group": results["intent_group"],
#     "high_confidence": results["high_confidence"],
#     "possible_intents": results["possible_intents"],
#     "explanation": explanation
# }
# from src.inference.predictor import predict_intent

# NEUTRAL_PHRASES = [
#     "okay", "ok", "fine", "thanks", "thank you",
#     "alright", "noted", "sure"
# ]
# clean_text = text.lower().strip()
# if clean_text in NEUTRAL_PHRASES:
#     return {
#         "final_intent": "neutral",
#         "intent_group": "neutral",
#         "high_confidence": [],
#         "possible_intents": [],
#         "is_ambiguous": False,
#         "explanation": "The text is a short acknowledgement with no hidden or indirect intent."
#     }
# INTENT_GROUPS = {
#     "agreement_related": [
#         "genuine_agreement",
#         "manipulative_agreement",
#         "fake_politeness"
#     ],
#     "disagreement_related": [
#         "indirect_disagreement",
#         "passive_aggression"
#     ],
#     "avoidance_related": [
#         "avoidance",
#         "stress_masking"
#     ],
#     "neutral": [
#         "neutral"
#     ]
# }

# INTENT_PRIORITY = [
#     "passive_aggression",
#     "manipulative_agreement",
#     "indirect_disagreement",
#     "fake_politeness",
#     "stress_masking",
#     "avoidance",
#     "genuine_agreement",
#     "neutral"
# ]


# def confidence_level(score):
#     if score >= 0.6:
#         return "High"
#     elif score >= 0.3:
#         return "Medium"
#     elif score >= 0.15:
#         return "Low"
#     else:
#         return "Very Low"

# def average_confidence(intents):
#     if not intents:
#         return 0
#     return sum(i["score"] for i in intents)/len(intents)
# avg_conf = average_confidence(enriched_possible)
# if avg_conf < 0.28:
#     final_intent = "neutral"


# def decide_final_intent(results):
#     all_intents = results["high_confidence"] + results["possible_intents"]

#     if not all_intents:
#         return "neutral"

#     for intent in INTENT_PRIORITY:
#         for item in all_intents:
#             if item["intent"] == intent:
#                 return intent

#     return "neutral"


# def generate_explanation(final_intent):
#     if final_intent == "neutral":
#         return "The text does not strongly indicate any hidden or indirect intent."

#     return (
#         f"The text shows linguistic patterns associated with '{final_intent}', "
#         f"such as indirect phrasing, controlled agreement, or masked emotion."
#     )

# def detect_ambiguity(possible_intents, margin=0.08):
#     if len(possible_intents)<2:
#         return False
#     sorted_intents = sorted(
#         possible_intents, key=lambda x: x["score"], reverse= True
#     )
#     return abs(sorted_intents[0]["score"] - sorted_intents[1]["score"])<=margin


# def predict_with_confidence(text):
#     base_result = predict_intent(text)

#     enriched_possible = []
#     enriched_high = []
#     group_scores = {}

#     # Enrich possible intents
#     for intent, score in base_result["possible_intents"]:
#         enriched_possible.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })

#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     # Enrich high confidence intents
#     for intent, score in base_result["high_confidence"]:
#         enriched_high.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })

#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     dominant_group = (
#         max(group_scores, key=group_scores.get)
#         if group_scores else "neutral"
#     )

#     results = {
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "intent_group": dominant_group,
#         "neutral": base_result["neutral"]
#     }

#     final_intent = decide_final_intent(results)
#     explanation = generate_explanation(final_intent)

#     return {
#         "final_intent": final_intent,
#         "intent_group": dominant_group,
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "explanation": explanation,
#         "is_ambiguous": detect_ambiguity(enriched_possible),
        
#     }
# def generate_explanation(final_intent, results):
#     if final_intent == "neutral":
#         return "The sentence appears direct and does not contain linguistic markers of hidden intent."

#     if results.get("is_ambiguous"):
#         return (
#             "The sentence exhibits mixed linguistic cues, suggesting multiple possible hidden intents "
#             "without a dominant signal."
#         )

#     return (
#         f"The sentence reflects communication patterns linked to '{final_intent}', "
#         "such as indirect phrasing, strategic agreement, or emotional masking."
#     )
# from src.inference.predictor import predict_intent


# # ---------------- CONSTANTS ---------------- #

# NEUTRAL_PHRASES = {
#     "okay", "ok", "fine", "thanks", "thank you",
#     "alright", "noted", "sure"
# }

# INTENT_GROUPS = {
#     "agreement_related": [
#         "genuine_agreement",
#         "manipulative_agreement",
#         "fake_politeness"
#     ],
#     "disagreement_related": [
#         "indirect_disagreement",
#         "passive_aggression"
#     ],
#     "avoidance_related": [
#         "avoidance",
#         "stress_masking"
#     ],
#     "neutral": ["neutral"]
# }

# INTENT_PRIORITY = [
#     "passive_aggression",
#     "manipulative_agreement",
#     "indirect_disagreement",
#     "fake_politeness",
#     "stress_masking",
#     "avoidance",
#     "genuine_agreement",
#     "neutral"
# ]

# CONFLICT_PAIRS = [
#     ("genuine_agreement", "passive_aggression"),
#     ("genuine_agreement", "indirect_disagreement"),
#     ("manipulative_agreementt", "genuine_agreement")
# ]


# # ---------------- HELPERS ---------------- #

# def confidence_level(score):
#     if score >= 0.6:
#         return "High"
#     elif score >= 0.3:
#         return "Medium"
#     elif score >= 0.15:
#         return "Low"
#     return "Very Low"


# def detect_conflict(intents):
#     intent_names = [i["intent"] for i in intents]
#     for a, b in CONFLICT_PAIRS:
#         if a in intent_names and b in intent_names:
#             return True
#         return False

# def detect_ambiguity(possible_intents, margin=0.08):
#     if len(possible_intents) < 2:
#         return False
#     sorted_scores = sorted(
#         [i["score"] for i in possible_intents],
#         reverse = True
#     )
#     return abs(sorted_scores[0]-sorted_scores[1])<margin
#     # sorted_intents = sorted(
#     #     possible_intents, key=lambda x: x["score"], reverse=True
#     # )
#     # return abs(sorted_intents[0]["score"] - sorted_intents[1]["score"]) <= margin


# def check_ambiguity(possible_intents, margin = 0.1):
#     if len(possible_intents)<2:
#         return False
#     sorted_intents = sorted(
#         possible_intents, key = lambda x: x["score"], reverse=True
#     )

#     top = sorted_intents[0]["score"]
#     second = sorted_intents[1]["score"]
#     return abs(top - second) <= margin


# def decide_final_intent(results):
#     all_intents = results["high_confidence"] + results["possible_intents"]

#     for intent in INTENT_PRIORITY:
#         for item in all_intents:
#             if item["intent"] == intent:
#                 return intent

#     return "neutral"


# def generate_explanation(final_intent, is_ambiguous):
#     if is_ambiguous:
#         return (
#             "The sentence contains mixed linguistic cues, indicating overlapping "
#             "hidden intents without a clear dominant signal."
#         )

#     if final_intent == "genuine_agreement":
#         return "The sentence expresses clear and direct agreement without hidden or conflicting intent."


#     if final_intent == "neutral":
#         return (
#             "The sentence appears direct and does not contain linguistic markers "
#             "of hidden or indirect intent."
#         )

#     return (
#         f"The sentence reflects communication patterns linked to '{final_intent}', "
#         "such as indirect phrasing, emotional masking, or strategic agreement."
#     )
# def sanitize_text(text):
#     if not isinstance(text, str):
#         return None, "Input must be a string"
#     text = text.strip()
#     if len(text)< 5:
#         return None, "Input too short for intent analysis"
#     return text, None
# def low_confidence_warning(final_intent, results):
#     if final_intent == "neutral":
#         return "No Strong intent detected"
#     scores = [
#         item["score"] for item in results["possible_intents"]
#         if item["intent"] == final_intent
#     ]
#     if scores and scores[0]<0.35:
#         return "Prediction confidence is moderate. Interpret Cautiously."
#     return None
# # ---------------- MAIN PREDICTOR ---------------- #

# def predict_with_confidence(text):
#     text, error = sanitize_text(text)
#     if error:
#         return{
#             "error": error,
#             "final_intent": "neutral"
#         }
#     base_result = predict_intent(text)

#     if not text or len(text.strip()) < 3:
#         return {"error": "Input too short or empty"}

#     clean_text = text.lower().strip()

#     # 🔹 Rule-based neutral shortcut

    
#     top_score = 0
#     if results["high_confidence"]:
#         top_score = results["high_confidence"][0]["score"]
#     elif results["possible_intents"]:
#         top_score = results["possible_intents"][0]["score"]

#     if top_score < 0.25:
#         final_intent = "ambiguous_intent"
#         is_ambiguous = True



#     if len(text.strip().split()) <= 1:
#         return {
#             "final_intent": "neutral",
#             "intent_group": "neutral",
#             "high_confidence": [],
#             "possible_intents": [],
#             "is_ambiguous": True,
#             "warning": "Very short utterance. Context required.",
#             "explanation": "Single-word responses require conversational context for intent detection."
#     }
#     if clean_text in NEUTRAL_PHRASES:
#         return {
#             "final_intent": "neutral",
#             "intent_group": "neutral",
#             "high_confidence": [],
#             "possible_intents": [],
#             "is_ambiguous": False,
#             "explanation": (
#                 "The text is a short acknowledgement with no hidden or indirect intent."
#             )
#         }

#     base_result = predict_intent(text)

#     enriched_possible = []
#     enriched_high = []
#     group_scores = {}

#     # Possible intents
#     for intent, score in base_result["possible_intents"]:
#         enriched_possible.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })

#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     # High confidence intents
#     for intent, score in base_result["high_confidence"]:
#         enriched_high.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })

#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     dominant_group = max(group_scores, key=group_scores.get) if group_scores else "neutral"

#     results = {
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "intent_group": dominant_group
#     }

#     is_ambiguous = detect_ambiguity(enriched_possible)
#     final_intent = decide_final_intent(results)
#     explanation = generate_explanation(final_intent, is_ambiguous)
#     is_ambiguouss = check_ambiguity(results["possible_intents"])
#     has_conflict = detect_conflict(results["possible_intents"])

#     warning = None
#     if has_conflict:
#         warning = "Conflicting communication signals detected."
#     elif is_ambiguouss:
#         warning = "Multiple intents detected with similar confidence."
#     elif all(i["confidence"] == "Medium" for i in results["possible_intents"]):
#         warning = "Prediction confidence is moderate. Interpret cautiously."

#     if warning or is_ambiguous:
#         reliability = "Low"
#     elif final_intent in [i["intent"] for i in high_confidence]:
#         reliability = "High"
#     else:
#         reliability = "Medium"


#     return {
#         "final_intent": final_intent,
#         "intent_group": dominant_group,
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "is_ambiguous": detect_ambiguity(enriched_possible),
#         "warning": low_confidence_warning(final_intent, results),
#         "explanation": explanation
#     }
from src.inference.predictor import predict_intent


# ---------------- CONSTANTS ---------------- #

HELP_SEEKING_PATTERNS = [
    "can you explain",
    "i need help",
    "what does this",
    "how do i",
    "can you help",
    "please explain",
    "i don't understand",
]

POLITE_NEUTRAL_PATTERNS = [
    "thank you",
    "thanks",
    "appreciate it",
    "good explanation",
]



STRONG_NEGATIVE_PATTERNS = [
    "useless",
    "nonsense",
    "worst",
    "never understand",
    "complete nonsense",
    "waste of time",
    "this is garbage",
]


NEUTRAL_PHRASES = {
    "okay", "ok", "fine", "thanks", "thank you",
    "alright", "noted", "sure"
}

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
    "neutral": ["neutral"]
}

INTENT_PRIORITY = [
    "passive_aggression",
    "manipulative_agreement",
    "indirect_disagreement",
    "fake_politeness",
    "stress_masking",
    "avoidance",
    "genuine_agreement",
    "neutral"
]

CONFLICT_PAIRS = [
    ("genuine_agreement", "passive_aggression"),
    ("genuine_agreement", "indirect_disagreement"),
    ("manipulative_agreement", "genuine_agreement")
]


# ---------------- HELPERS ---------------- #

def confidence_level(score):
    if score >= 0.6:
        return "High"
    elif score >= 0.3:
        return "Medium"
    elif score >= 0.15:
        return "Low"
    return "Very Low"


def detect_conflict(intents):
    intent_names = {i["intent"] for i in intents}
    for a, b in CONFLICT_PAIRS:
        if a in intent_names and b in intent_names:
            return True
    return False


def detect_ambiguity(possible_intents, margin=0.08):
    if len(possible_intents) < 2:
        return False
    sorted_scores = sorted(
        [i["score"] for i in possible_intents],
        reverse=True
    )
    return abs(sorted_scores[0] - sorted_scores[1]) <= margin


# def decide_final_intent(results):
#     all_intents = results["high_confidence"] + results["possible_intents"]
#     for intent in INTENT_PRIORITY:
#         for item in all_intents:
#             if item["intent"] == intent:
#                 return intent
#     return "neutral"
def decide_final_intent(results, threshold=0.5):
    all_intents = results["high_confidence"] + results["possible_intents"]

    if not all_intents:
        return "neutral"

    # pick highest score
    top_intent = max(all_intents, key=lambda x: x["score"])

    # confidence gating
    if top_intent["score"] < threshold:
        return "neutral"

    return top_intent["intent"]


def generate_explanation(final_intent, is_ambiguous):
    if is_ambiguous:
        return (
            "The sentence contains overlapping linguistic cues, "
            "making the dominant intent unclear."
        )

    explanations = {
        "genuine_agreement": "Clear and direct agreement without hidden intent.",
        "neutral": "The sentence contains no strong linguistic signals of hidden intent."
    }

    return explanations.get(
        final_intent,
        f"The sentence reflects communication patterns linked to '{final_intent}'."
    )


def sanitize_text(text):
    if not isinstance(text, str):
        return None, "Input must be a string"
    text = text.strip()
    if len(text) < 3:
        return None, "Input too short for intent analysis"
    return text, None


def low_confidence_warning(final_intent, results):
    scores = [
        i["score"] for i in results["possible_intents"]
        if i["intent"] == final_intent
    ]
    if scores and scores[0] < 0.35:
        return "Prediction confidence is moderate. Interpret cautiously."
    return None



# ---------------- MAIN ---------------- #

# def predict_with_confidence(text):
#     text, error = sanitize_text(text)
#     if error:
#         return {"error": error, "final_intent": "neutral"}

#     clean_text = text.lower().strip()

#     if clean_text in NEUTRAL_PHRASES or len(text.split()) == 1:
#         return {
#             "final_intent": "neutral",
#             "intent_group": "neutral",
#             "high_confidence": [],
#             "possible_intents": [],
#             "is_ambiguous": False,
#             "warning": None,
#             "explanation": "Short acknowledgement without hidden intent."
#         }

#     base_result = predict_intent(text)

#     enriched_high = []
#     enriched_possible = []
#     group_scores = {}

#     for intent, score in base_result["high_confidence"]:
#         enriched_high.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })
#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     for intent, score in base_result["possible_intents"]:
#         enriched_possible.append({
#             "intent": intent,
#             "score": score,
#             "confidence": confidence_level(score)
#         })
#         for group, intents in INTENT_GROUPS.items():
#             if intent in intents:
#                 group_scores[group] = group_scores.get(group, 0) + score

#     dominant_group = max(group_scores, key=group_scores.get) if group_scores else "neutral"

#     results = {
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "intent_group": dominant_group
#     }

#     # is_ambiguous = detect_ambiguity(enriched_possible)
#     all_intents = enriched_high + enriched_possible
#     is_ambiguous = detect_ambiguity(all_intents)

#     has_conflict = detect_conflict(enriched_possible)
#     final_intent = decide_final_intent(results)
    
    

#     warning = None
#     if has_conflict:
#         warning = "Conflicting communication signals detected."
#     elif is_ambiguous:
#         warning = "Multiple intents detected with similar confidence."
#     elif enriched_possible and all(i["confidence"] == "Medium" for i in enriched_possible):
#         warning = "Prediction confidence is moderate. Interpret cautiously."
#     return {
#         "final_intent": final_intent,
#         "intent_group": dominant_group,
#         "high_confidence": enriched_high,
#         "possible_intents": enriched_possible,
#         "is_ambiguous": is_ambiguous,
#         "warning": warning or low_confidence_warning(final_intent, results),
#         "explanation": generate_explanation(final_intent, is_ambiguous)
#     }
HELP_SEEKING_PATTERNS = [
    "can you explain",
    "i need help",
    "what does this",
    "how do i",
    "can you help",
    "please explain",
    "i don't understand",
]

POLITE_NEUTRAL_PATTERNS = [
    "thank you",
    "thanks",
    "appreciate it",
    "good explanation",
]
COMPLAINT_PATTERNS = [
    "broken",
    "not working",
    "doesn't work",
    "waste",
    "useless",
    "terrible"
]

FRUSTRATION_PATTERNS = [
    "i'm done",
    "im done",
    "forget it",
    "whatever",
    "leave it"
]

def neutral_override_response(reason):
    return {
        "final_intent": "neutral",
        "intent_group": "neutral",
        "high_confidence": [{
            "intent": "neutral",
            "score": 0.95,
            "confidence": "High"
        }],
        "possible_intents": [],
        "is_ambiguous": False,
        "warning": None,
        "explanation": reason
    }

def predict_with_confidence(text, decision_threshold=0.5, ambiguity_margin=0.07):
    
    
    
    
    text, error = sanitize_text(text)
    if error:
        return {"error": error, "final_intent": "neutral"}

    clean_text = text.lower().strip()

    # -------------------------
    # 1️⃣ Simple Neutral Override
    # -------------------------
    if clean_text in NEUTRAL_PHRASES or len(clean_text.split()) <= 2:
        return {
            "final_intent": "neutral",
            "intent_group": "neutral",
            "high_confidence": [],
            "possible_intents": [],
            "is_ambiguous": False,
            "warning": None,
            "explanation": "Short acknowledgement without hidden intent."
        }
    
    for phrase in HELP_SEEKING_PATTERNS:
        if phrase in clean_text:
            return neutral_override_response(
                "Clear help-seeking intent detected."
            )
        
    for phrase in POLITE_NEUTRAL_PATTERNS:
        if phrase in clean_text:
            return neutral_override_response(
                "Clear polite acknowledgment detected."
            )
    for phrase in COMPLAINT_PATTERNS:
        if phrase in clean_text:
            return {
                "final_intent": "passive_aggression",
                "intent_group": "disagreement_related",
                "high_confidence": [{
                    "intent": "passive_aggression",
                    "score": 0.9,
                    "confidence": "High"
                }],
                "possible_intents": [],
                "is_ambiguous": False,
                "warning": None,
                "explanation": "Complaint language detected indicating dissatisfaction."
            }
    for phrase in FRUSTRATION_PATTERNS:
        if phrase in clean_text:
            return {
                "final_intent": "passive_aggression",
                "intent_group": "disagreement_related",
                "high_confidence": [{
                    "intent": "passive_aggression",
                    "score": 0.9,
                    "confidence": "High"
                }],
                "possible_intents": [],
                "is_ambiguous": False,
                "warning": None,
                "explanation": "Frustration or resignation language detected."
            }
    for phrase in STRONG_NEGATIVE_PATTERNS:
        if phrase in clean_text:
            return {
                "final_intent": "passive_aggression",
                "intent_group": "disagreement_related",
                "high_confidence": [{
                    "intent": "passive_aggression",
                    "score": 0.95,
                    "confidence": "High"
                }],
                "possible_intents": [],
                "is_ambiguous": False,
                "warning": None,
                "explanation": "Strong negative language detected indicating direct dissatisfaction."
            }

    # -------------------------
    # 2️⃣ Model Prediction
    # -------------------------
    # -------------------------
    # 2️⃣ Model Prediction
    # -------------------------
    base_result = predict_intent(text)

    enriched_intents = []
    group_scores = {}

    # Combine high + possible into single list
    for intent, score in base_result["high_confidence"] + base_result["possible_intents"]:
        enriched = {
            "intent": intent,
            "score": score,
            "confidence": confidence_level(score)
        }
        enriched_intents.append(enriched)

        # group scoring
        for group, intents in INTENT_GROUPS.items():
            if intent in intents:
                group_scores[group] = group_scores.get(group, 0) + score

    if not enriched_intents:
        return {
            "final_intent": "neutral",
            "intent_group": "neutral",
            "high_confidence": [],
            "possible_intents": [],
            "is_ambiguous": False,
            "warning": "Model returned no confident predictions.",
            "explanation": "No strong intent detected."
        }

    # -------------------------
    # 3️⃣ Sort by score
    # -------------------------
    enriched_intents.sort(key=lambda x: x["score"], reverse=True)
    top_intent = enriched_intents[0]
    top_score = top_intent["score"]

    # -------------------------
    # 4️⃣ Threshold Gating
    # -------------------------
    if top_score < decision_threshold:
        final_intent = "neutral"
    else:
        final_intent = top_intent["intent"]

    # -------------------------
    # 5️⃣ Ambiguity Detection
    # -------------------------
    is_ambiguous = False
    if len(enriched_intents) > 1:
        second_score = enriched_intents[1]["score"]
        if abs(top_score - second_score) <= ambiguity_margin:
            is_ambiguous = True

    # -------------------------
    # 6️⃣ Conflict Detection
    # -------------------------
    has_conflict = detect_conflict(enriched_intents)

    # -------------------------
    # 7️⃣ Dominant Group
    # -------------------------
    dominant_group = (
        max(group_scores, key=group_scores.get)
        if group_scores
        else "neutral"
    )

    # -------------------------
    # 8️⃣ Warning Logic
    # -------------------------
    warning = None

    if has_conflict:
        warning = "Conflicting communication signals detected."
    elif is_ambiguous:
        warning = "Top intents have very close scores."
    elif top_score < 0.6:
        warning = "Prediction confidence is moderate."

    # -------------------------
    # 9️⃣ Explanation
    # -------------------------
    explanation = generate_explanation(final_intent, is_ambiguous)

    return {
        "final_intent": final_intent,
        "intent_group": dominant_group,
        "high_confidence": [
            i for i in enriched_intents if i["confidence"] == "High"
        ],
        "possible_intents": [
            i for i in enriched_intents if i["confidence"] != "High"
        ],
        "is_ambiguous": is_ambiguous,
        "warning": warning,
        "explanation": explanation
    }
