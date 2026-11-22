def find_tuples(test_list, k):
    """Return the tuples from test_list in which every element is divisible by k.

    Parameters
    ----------
    test_list : list of tuple
        List containing tuples of integers.
    k : int
        Non-zero integer divisor.

    Returns
    -------
    list of tuple
        Tuples whose elements are all divisible by k.

    Raises
    ------
    TypeError
        If test_list is not a list of tuples of integers, or k is not an integer.
    ValueError
        If k is zero.
    """
    if not isinstance(test_list, list):
        raise TypeError("test_list must be a list of tuples")
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k == 0:
        raise ValueError("k must be a non-zero integer")

    result = []
    for index, item in enumerate(test_list):
        if not isinstance(item, tuple):
            raise TypeError("element at index {} is not a tuple".format(index))
        for value in item:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(
                    "tuple at index {} contains a non-integer element".format(index)
                )
        if all(value % k == 0 for value in item):
            result.append(item)
    return result


if __name__ == "__main__":
    sample = [(6, 24, 12), (7, 9, 11), (12, 24, 36)]
    print(find_tuples(sample, 6))
