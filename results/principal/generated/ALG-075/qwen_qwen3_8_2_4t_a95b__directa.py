def find_tuples(lst, k):
    if k == 0:
        return []
    return [t for t in lst if all(x % k == 0 for x in t)]
