import re

EXIT_KEYWORDS = {"exit", "quit", "stop", "end", "close"}

def normalize_text(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text.lower()).strip()

def is_exit_command(text: str) -> bool:
    if not text:
        return False
    clean = normalize_text(text)
    return clean in EXIT_KEYWORDS