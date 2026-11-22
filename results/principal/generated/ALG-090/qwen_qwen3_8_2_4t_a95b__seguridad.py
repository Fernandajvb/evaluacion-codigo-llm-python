def longest_word_length(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()
    if not words:
        return 0

    return max(len(word) for word in words)
