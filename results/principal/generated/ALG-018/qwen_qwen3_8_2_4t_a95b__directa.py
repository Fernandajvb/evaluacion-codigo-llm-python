def remove_characters(first_string, second_string):
    chars_to_remove = set(second_string)
    return ''.join(char for char in first_string if char not in chars_to_remove)
