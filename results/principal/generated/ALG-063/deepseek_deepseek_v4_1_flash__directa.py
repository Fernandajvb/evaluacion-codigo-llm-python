def max_difference(tuple_list):
    return max(abs(a - b) for a, b in tuple_list) if tuple_list else 0
