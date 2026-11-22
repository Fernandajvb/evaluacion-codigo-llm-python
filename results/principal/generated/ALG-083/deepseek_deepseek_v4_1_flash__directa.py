def find_char(s):
    return chr(sum(ord(c) for c in s) % 26 + ord('a'))
