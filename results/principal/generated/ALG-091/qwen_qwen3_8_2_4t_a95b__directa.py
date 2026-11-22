def check_substring_in_list(substring, string_list):
    return any(substring in value for value in string_list)
