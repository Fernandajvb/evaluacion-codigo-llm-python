def is_substring_present(s, strings):
    return any(s in string for string in strings)
