def max_difference(tuple_list):
    if not isinstance(tuple_list, (list, tuple)):
        raise TypeError("Input must be a list or tuple of tuples.")
    max_diff = None
    for item in tuple_list:
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise ValueError("Each element must be a tuple or list of exactly two numbers.")
        a, b = item
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Tuple elements must be numbers.")
        diff = abs(a - b)
        if max_diff is None or diff > max_diff:
            max_diff = diff
    return max_diff
