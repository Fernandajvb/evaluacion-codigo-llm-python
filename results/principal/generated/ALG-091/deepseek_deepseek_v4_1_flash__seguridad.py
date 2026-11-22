def is_substring_in_list(substring, strings):
    if not isinstance(substring, str):
        raise TypeError("substring must be a string")
    if not isinstance(strings, list):
        raise TypeError("strings must be a list")
    for value in strings:
        if not isinstance(value, str):
            raise TypeError("all elements in strings must be strings")
    return any(substring in value for value in strings)
