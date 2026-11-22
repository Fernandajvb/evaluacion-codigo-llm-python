def get_Char(str):
    total = 0
    for ch in str:
        total += ord(ch)
    return chr(total % 26)
