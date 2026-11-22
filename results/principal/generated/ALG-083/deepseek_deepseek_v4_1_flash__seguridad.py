def ascii_sum_mod26(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    total = sum(ord(ch) for ch in s)
    return chr(ord('a') + (total % 26))
