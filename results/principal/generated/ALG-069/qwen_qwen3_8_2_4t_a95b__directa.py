def contains_sublist(lst, sublist):
    if not sublist:
        return True
    n = len(sublist)
    return any(lst[i:i + n] == sublist for i in range(len(lst) - n + 1))
