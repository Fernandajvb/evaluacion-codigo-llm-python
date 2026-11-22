def find_character(s: str) -> str:
    return chr(ord('a') + (sum(ord(c) for c in s) % 26))

getChar = find_character
