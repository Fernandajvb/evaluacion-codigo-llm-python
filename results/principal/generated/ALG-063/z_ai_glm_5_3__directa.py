def max_difference(test_list):
    res = max((abs(x - y)) for x, y in test_list)
    return res
