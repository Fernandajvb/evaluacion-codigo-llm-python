def find_tuples_divisible_by_k(tuples_list, k):
    if not isinstance(tuples_list, list):
        raise TypeError("tuples_list must be a list")
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k must be an integer")
    if k == 0:
        raise ValueError("k must not be zero")

    result = []
    for item in tuples_list:
        if not isinstance(item, tuple):
            raise TypeError("All items in tuples_list must be tuples")
        for value in item:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("All tuple elements must be integers")
        if all(value % k == 0 for value in item):
            result.append(item)
    return result
