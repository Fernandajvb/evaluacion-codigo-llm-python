def remove_dirty_chars(str1, str2):
    chars_to_remove = set(str2)
    return ''.join(char for char in str1 if char not in chars_to_remove)
