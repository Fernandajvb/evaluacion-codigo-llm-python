def remove_characters(first: str, second: str) -> str:
    if not isinstance(first, str) or not isinstance(second, str):
        raise TypeError("Both arguments must be strings")
    chars_to_remove = set(second)
    return "".join(char for char in first if char not in chars_to_remove)
