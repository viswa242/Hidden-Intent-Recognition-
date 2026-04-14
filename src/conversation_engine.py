INTENT_WEIGHTS = {
    "passive_aggression": 2.0,
    "manipulative_agreement": 2.5,
    "indirect_disagreement": 1.8,
    "fake_politeness": 1.5,
    "stress_masking": 1.2,
    "avoidance": 1.3,
    "genuine_agreement": 0.5,
    "neutral": 0.2
}

# class ConversationEngine:
#     def __init__(self):
#         self.history = []
#         self.total_score = 0
#         self.intent_counts = {}

#     def update(self, final_intent):
#         self.history.append(final_intent)

#         weight = INTENT_WEIGHTS.get(final_intent, 0)
#         self.total_score += weight

#         self.intent_counts[final_intent] =(
#             self.intent_counts.get(final_intent,0)+1
#         )

#     def get_escalation_level(self):
#         avg_score = self.total_score / max(len(self.history), 1)

#         if avg_score >= 2:
#             return "High Escalation"
#         elif avg_score >= 1.2:
#             return "Moderate Escalation"
#         else:
#             return "Low Escalation"
    
#     def get_dominant_pattern(self):
#         if not self.intent_counts:
#             return "No pattern detected"
        
#         return max(self.intent_counts, key=self.intent_counts.get)
    
#     def get_summary(self):
#         return {
#             "total_messages": len(self.history),
#             "dominant_pattern": self.get_dominant_pattern(),
#             "escalation_level": self.get_escalation_level(),
#             "psychological_score": round(self.total_score,2)
#         }
# import uuid
# class ConversationEngine:
#     def __init__(self):
#         self.start_new_session()
#         self.score_history = []


#     def start_new_session(self):
#         self.session_id = str(uuid.uuid4())[:8]
#         self.history = []
#         self.total_score = 0
#         self.score_history = []

#     def reset_session(self):
#         summary = self.get_summary()
#         self.start_new_session()
#         return summary
    
#     def add_message(self, final_intent):
#         weights = {
#             "passive_aggression":2.0,
#             "manipulative_agreement":2.5,
#             "indirect_disagreement":1.5,
#             "fake_politeness":1.8,
#             "stress_masking": 1.2,
#             "avoidance": 1.0,
#             "genuine_agreement": 0.5,
#             "neutral": 0
#         }
#         score = weights.get(final_intent,0)
#         recent_history = self.history[-2:]  # last two messages

#         if recent_history.count("passive_aggression") >= 2:
#             if final_intent in ["passive_aggression", "indirect_disagreement"]:
#                 score += 1  # small escalation boost

        
#         self.total_score += score
#         self.history.append(final_intent)
#         self.score_history.append(score)
        



#     def get_trend(self):
#         if len(self.score_history)<2:
#             return "Insufficient Data"
#         elif self.score_history[-1]>self.score_history[-2]:
#             return "Decreasing"
#         else:
#             return "Stable"
    


#     # def get_repetition_ratio(self):
#     #     if not self.history:
#     #         return 0
#     #     dominant_pattern = max(set(self.history), key=self.history.count)
#     #     return round(self.history.count(dominant_pattern)/len(self.history),2)
#     def calculate_dominant_pattern(self):
#         if not self.history:
#             return None
    
#         dominant = max(set(self.history), key=self.history.count)
#         return dominant
    
#     def calculate_dominant_pattern(self):
#         if not self.history:
#             return None, 0
    
#         dominant = max(set(self.history), key=self.history.count)
#         ratio = round(self.history.count(dominant)/len(self.history),2)
#         return dominant, ratio



#     def calculate_trend(self):
#         if len(self.score_history) < 2:
#             return "Stable"

#         midpoint = len(self.score_history) // 2
#         first_half = self.score_history[:midpoint]
#         second_half = self.score_history[midpoint:]

#         if not first_half or not second_half:
#             return "Stable"

#         avg_first = sum(first_half) / len(first_half)
#         avg_second = sum(second_half) / len(second_half)

#         if avg_second > avg_first:
#             return "Escalating"
#         elif avg_second < avg_first:
#             return "De-escalating"
#         else:
#             return "Stable"


#     def get_summary(self):
        
#         if not self.history:
#             return{
#                 "session_id": self.session_id,
#                 "message": "No conversation data available."

#             }
        
#         # dominant_pattern = max(set(self.history), key=self.history.count)
#         dominant_pattern, dominance_ratio = self.calculate_dominant_pattern()

#         avg_score = self.total_score #/len(self.history)

#         if avg_score >=8:
#             escalation = "High Escalation"
#         elif avg_score >=4:
#             escalation = "Moderate Escalation"
#         else:
#             escalation = "Low Escalation"
        
#         trend = self.calculate_trend()

#         # repetition_ratio = self.get_repetition_ratio()

#         if escalation == "High Escalation" and trend == "Increasing" and repetition_ratio >0.6:
#             risk_level = "Critical conversation"
#         elif escalation == "High Escalation":
#             risk_level = "Monitor Closely"
#         else:
#             risk_level = "Normal"
#         print("Score history:", self.score_history)
#         return {
#             "session_id": self.session_id,
#             "total_messages": len(self.history),
#             "dominant_pattern": dominant_pattern,
#             "escalation_level": escalation,
#             "trend": trend,
#             "repetition_ratio": repetition_ratio,
#             "risk_level": risk_level,
#             "psychological_score": round(self.total_score, 2)
#         }
# import uuid

# class ConversationEngine:

#     def __init__(self):
#         self.start_new_session()

#     def start_new_session(self):
#         self.session_id = str(uuid.uuid4())[:8]
#         self.history = []
#         self.total_score = 0
#         self.score_history = []

#     def reset_session(self):
#         summary = self.get_summary()
#         self.start_new_session()
#         return summary

#     def add_message(self, final_intent):

#         weights = {
#             "passive_aggression": 2.0,
#             "manipulative_agreement": 2.5,
#             "indirect_disagreement": 1.5,
#             "fake_politeness": 1.8,
#             "stress_masking": 1.2,
#             "avoidance": 1.0,
#             "genuine_agreement": 0.5,
#             "neutral": 0
#         }

#         score = weights.get(final_intent, 0)

#         # Escalation boost logic
#         recent_history = self.history[-2:]
#         if recent_history.count("passive_aggression") >= 2:
#             if final_intent in ["passive_aggression", "indirect_disagreement"]:
#                 score += 1

#         self.total_score += score
#         self.history.append(final_intent)
#         self.score_history.append(score)

#     # -------------------------
#     # Dominant Pattern + Ratio
#     # -------------------------
#     def calculate_dominant_pattern(self):
#         if not self.history:
#             return None, 0

#         dominant = max(set(self.history), key=self.history.count)
#         ratio = round(self.history.count(dominant) / len(self.history), 2)
#         return dominant, ratio

#     # -------------------------
#     # Trend Detection
#     # -------------------------
#     def calculate_trend(self):
#         if len(self.score_history) < 2:
#             return "Stable"

#         midpoint = len(self.score_history) // 2
#         first_half = self.score_history[:midpoint]
#         second_half = self.score_history[midpoint:]

#         if not first_half or not second_half:
#             return "Stable"

#         avg_first = sum(first_half) / len(first_half)
#         avg_second = sum(second_half) / len(second_half)

#         if avg_second > avg_first:
#             return "Escalating"
#         elif avg_second < avg_first:
#             return "De-escalating"
#         else:
#             return "Stable"

#     # -------------------------
#     # Summary
#     # -------------------------
#     def get_summary(self):

#         if not self.history:
#             return {
#                 "session_id": self.session_id,
#                 "message": "No conversation data available."
#             }

#         dominant_pattern, dominance_ratio = self.calculate_dominant_pattern()

#         # Use average score (IMPORTANT)
#         avg_score = self.total_score / len(self.history)

#         if avg_score >= 2:
#             escalation = "High Escalation"
#         elif avg_score >= 1:
#             escalation = "Moderate Escalation"
#         else:
#             escalation = "Low Escalation"

#         trend = self.calculate_trend()
#         # total_messages = len(self.history)
#         # if escalation == "High Escalation" and trend == "Escalating" and dominance_ratio > 0.6:
#         #     risk_level = "Critical Conversation"
#         # elif escalation == "High Escalation":
#         #     risk_level = "Monitor Closely"
#         # else:
#         #     risk_level = "Normal"
#         # if (
#         #     total_messages >= 5 and
#         #     escalation == "High Escalation" and
#         #     trend == "Escalating" and
#         #     dominance_ratio > 0.6
#         #     ):
#         #     risk_level = "Critical Conversation"

#         # elif escalation == "High Escalation":
#         #     risk_level = "Monitor Closely"

#         # else:
#         #     risk_level = "Normal"
#         psychological_score = round(self.total_score, 2)
#         if psychological_score >= 10:
#             risk_level = "Critical Conversation"

#         elif escalation == "High Escalation" and dominance_ratio >= 0.6:
#             risk_level = "Monitor Closely"

#         elif psychological_score >= 6:
#             risk_level = "Elevated Risk"

#         else:
#             risk_level = "Normal"

        
#         print(f"Escalation: '{escalation}'")
#         print(f"Trend: '{trend}'")

#         print("Score history:", self.score_history)
#         return {
#             "session_id": self.session_id,
#             "total_messages": len(self.history),
#             "dominant_pattern": dominant_pattern,
#             "dominance_ratio": dominance_ratio,
#             "escalation_level": escalation,
#             "trend": trend,
#             "risk_level": risk_level,
#             "psychological_score": round(self.total_score, 2)
#         }

from src.session_id import SessionStore
from src.session_manager import SessionManager
import uuid


class ConversationEngine:

    # def __init__(self):
    #     self.start_new_session()
    def __init__(self, session_id=None):
        self.store = SessionStore()
        self.active = True
        # self.session = SessionManager(session_id)
        # self.conversation = self.session.load_conversation()

        if session_id:
            loaded = self.store.load_session(session_id)
            if loaded:
                self.session_id = session_id
                self.history = loaded["history"]
                self.score_history = loaded["score_history"]
                self.total_score = loaded["total_score"]
                return

        self.start_new_session()


    # -------------------------
    # Session Handling
    # -------------------------
    def start_new_session(self):
        self.session_id = str(uuid.uuid4())[:8]
        self.history = []
        self.score_history = []
        self.total_score = 0.0

    def reset_session(self):
        # summary = self.get_summary()
        # self.start_new_session()
        # return summary
        summary = self.get_summary()

    # Clear in-memory
        self.history = []
        self.score_history = []
        self.total_score = 0.0

    # Create NEW session ID
        self.session_id = str(uuid.uuid4())[:8]

    # Clear conversation store
        self.conversation = []
        self.session = SessionManager(self.session_id)

        return summary

    


    # -------------------------
    # Message Intake
    # -------------------------
    
        # -------------------------
    # Context Weighting (Day-23)
    # -------------------------
    def calculate_context_weight(self):
        """
        Determines how much the recent conversation context
        should influence the next message.
        """

        if len(self.history) < 2:
            return 1.0  # no context influence yet

        recent = self.history[-3:]  # last 3 intents
        dominant = max(set(recent), key=recent.count)

        # Base multiplier
        context_weight = 1.0

        # Negative dominant context
        if dominant in ["passive_aggression", "indirect_disagreement"]:
            context_weight = 1.2

        # Suppressed negativity (neutral after negativity)
        if recent[-1] == "neutral" and dominant != "neutral":
            context_weight = 1.15

        # Trend-aware adjustment
        trend = self.calculate_trend()
        if trend == "Escalating":
            context_weight += 0.1
        elif trend == "De-escalating":
            context_weight -= 0.1

        return round(max(context_weight, 0.8), 2)
    
    
    
    # def add_message(self, final_intent):

    #     weights = {
    #         "passive_aggression": 2.0,
    #         "manipulative_agreement": 2.5,
    #         "indirect_disagreement": 1.5,
    #         "fake_politeness": 1.8,
    #         "stress_masking": 1.2,
    #         "avoidance": 1.0,
    #         "genuine_agreement": 0.5,
    #         "neutral": 0.0
    #     }

    #     score = weights.get(final_intent, 0.0)

    #     # Escalation boost (pattern reinforcement only)
    #     recent = self.history[-2:]
    #     if recent.count("passive_aggression") == 2 and final_intent == "passive_aggression":
    #         score += 1.0

    #     self.history.append(final_intent)
    #     self.score_history.append(score)
    #     self.total_score += score
    def add_message(self, final_intent):
        if not self.active or self.session_id is None:
            return

        weights = {
            "passive_aggression": 2.0,
            "manipulative_agreement": 2.5,
            "indirect_disagreement": 1.5,
            "fake_politeness": 1.8,
            "stress_masking": 1.2,
            "avoidance": 1.0,
            "genuine_agreement": 0.5,
            "neutral": 0
        }

        base_score = weights.get(final_intent, 0)

        # Escalation boost logic (existing)
        recent_history = self.history[-2:]
        if recent_history.count("passive_aggression") >= 2:
            if final_intent in ["passive_aggression", "indirect_disagreement"]:
                base_score += 1

        # -------------------------
        # Context Weight Application
        # -------------------------
        context_weight = self.calculate_context_weight()
        final_score = round(base_score * context_weight, 2)

        self.total_score += final_score
        self.history.append(final_intent)
        self.score_history.append(final_score)
        # self.conversation.append(final_intent)
        # self.session.save_conversation(self.conversation)
        
        self.store.save_session(
            self.session_id,
            self.history,
            self.score_history,
            self.total_score
        )




    def apply_context_decay(self):
        """
        Applies decay so older scores have less influence
        """
        decay_factor = 0.85
        decayed_scores = []

        for i, score in enumerate(reversed(self.score_history)):
            decayed_scores.append(score * (decay_factor ** i))

        return list(reversed(decayed_scores))





    # -------------------------
    # Dominant Pattern
    # -------------------------
    def calculate_dominant_pattern(self):
        if not self.history:
            return None, 0.0

        dominant = max(set(self.history), key=self.history.count)
        ratio = round(self.history.count(dominant) / len(self.history), 2)
        return dominant, ratio

    # -------------------------
    # Trend Detection
    # -------------------------
    def calculate_trend(self):
        if len(self.score_history) < 2:
            return "Stable"

        mid = len(self.score_history) // 2
        first = self.score_history[:mid]
        second = self.score_history[mid:]

        if not first or not second:
            return "Stable"

        avg_first = sum(first) / len(first)
        avg_second = sum(second) / len(second)

        if avg_second > avg_first:
            return "Escalating"
        elif avg_second < avg_first:
            return "De-escalating"
        else:
            return "Stable"

    # -------------------------
    # Summary / Risk Engine
    # -------------------------
    
    def replay_session(self):
        return self.session.history()

    def validate_scores(self):
        return sum(self.session.score_history) == self.session.total_score
    
    
    def generate_alert(self, summary):
        risk = summary["risk_level"]
        escalation = summary["escalation_level"]

        if risk == "Critical Conversation":
            return {
            "alert_level": "CRITICAL",
            "message": "Immediate intervention recommended. High emotional escalation detected."
            }

        elif risk == "Monitor Closely":
            return {
            "alert_level": "WARNING",
            "message": "Conversation shows high escalation. Monitor user closely."
            }

        else:
            return {
            "alert_level": "NORMAL",
            "message": "Conversation is stable."
            }

    # def end_session(self):
    #     """
    #     Explicitly closes the current session so it cannot be reused.
    #     """
    #     self.active = False


    def end_session(self):
        self.active = False
        self.history = []
        self.score_history = []
        self.total_score = 0.0
        self.session_id = None

    def get_summary(self):

        if not self.history:
            return {
                "session_id": self.session_id,
                "message": "No conversation data available."
            }

        dominant_pattern, dominance_ratio = self.calculate_dominant_pattern()
        trend = self.calculate_trend()

        # avg_score = self.total_score / len(self.history)
        decayed_scores = self.apply_context_decay()
        avg_score = sum(decayed_scores) / len(decayed_scores)

        psychological_score = round(self.total_score, 2)


        
        # Escalation level (AVG based – stable)
        if avg_score >= 2.0:
            escalation = "High Escalation"
        elif avg_score >= 1.0:
            escalation = "Moderate Escalation"
        else:
            escalation = "Low Escalation"

        # -------------------------
        # Risk Level (FINAL RULESET)
        # -------------------------
        risk_level = "Normal"
        if (
            escalation == "High Escalation"
            and trend == "Escalating"
            and dominance_ratio > 0.6
        ):
            risk_level = "Critical Conversation"

        elif escalation == "High Escalation":
            risk_level = "Monitor Closely"
        
        alert = self.generate_alert({
            "risk_level": risk_level,
            "escalation_level": escalation
            })

        # Debug visibility (keep for now)
        print(f"Escalation: '{escalation}'")
        print(f"Trend: '{trend}'")
        print("Score history:", self.score_history)
        print("Session ID:", self.session_id)
        print("Total Score:", self.total_score)
        print("Messages:", len(self.history))

        return {
            "session_id": self.session_id,
            "total_messages": len(self.history),
            "dominant_pattern": dominant_pattern,
            "dominance_ratio": dominance_ratio,
            "escalation_level": escalation,
            "trend": trend,
            "risk_level": risk_level,
            "psychological_score": psychological_score,
            "alert": alert
        }
