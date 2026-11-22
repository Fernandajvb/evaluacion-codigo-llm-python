import re

def longest_word_length(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)
    return max((len(word) for word in words), default=0)
