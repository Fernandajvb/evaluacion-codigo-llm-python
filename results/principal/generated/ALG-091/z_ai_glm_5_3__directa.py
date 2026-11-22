def is_Substring(sub_str, list_str):
    for item in list_str:
        if sub_str in item:
            return True
    return False
