def contains_sublist(lst, sublist):
    if not sublist:
        return True
    n, m = len(lst), len(sublist)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublist:
            return True
    return False
