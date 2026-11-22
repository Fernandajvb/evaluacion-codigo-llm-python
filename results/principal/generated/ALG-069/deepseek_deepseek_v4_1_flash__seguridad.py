def contains_sublist(lst, sublist):
    if not isinstance(lst, list) or not isinstance(sublist, list):
        raise TypeError("Both arguments must be lists")
    n = len(lst)
    m = len(sublist)
    if m == 0:
        return True
    if m > n:
        return False
    for i in range(n - m + 1):
        if lst[i:i + m] == sublist:
            return True
    return False
