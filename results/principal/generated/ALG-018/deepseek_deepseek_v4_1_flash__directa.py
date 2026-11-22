def remove_chars(first, second):
    remove = set(second)
    return ''.join(ch for ch in first if ch not in remove)
