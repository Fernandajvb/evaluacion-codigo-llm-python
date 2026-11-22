def is_sublist(main_list, sublist):
    if not sublist:
        return True
    if len(sublist) > len(main_list):
        return False
    n = len(sublist)
    for i in range(len(main_list) - n + 1):
        if main_list[i:i + n] == sublist:
            return True
    return False
