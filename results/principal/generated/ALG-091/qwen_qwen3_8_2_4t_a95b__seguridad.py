def is_substring_in_list(substring, values):
    if not isinstance(substring, str):
        raise TypeError("substring must be a string")
    if not isinstance(values, list):
        raise TypeError("values must be a list")
    for value in values:
        if not isinstance(value, str):
            raise TypeError("all items in values must be strings")
        if substring in value:
            return True
    return False
