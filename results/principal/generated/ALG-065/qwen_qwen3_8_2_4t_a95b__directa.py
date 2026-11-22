def flatten_and_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += flatten_and_sum(item)
        else:
            total += item
    return total
