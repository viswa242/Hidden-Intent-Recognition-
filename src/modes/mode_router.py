from src.modes.mode_type import ModeType
from src.modes.mode1 import SingleSentenceMode
from src.modes.mode2 import AdvancedConversationMode

single_mode = SingleSentenceMode()
advanced_mode = AdvancedConversationMode()

def route_mode(mode: ModeType, engine, text: str, session_id: str | None):
    if mode == ModeType.SINGLE:
        return single_mode.process(engine, text)

    if mode == ModeType.ADVANCED:
        if not session_id:
            raise ValueError("session_id required for advanced mode")
        return advanced_mode.process(engine, session_id, text)

    raise ValueError("Invalid mode selected")