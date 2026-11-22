def find_tuples(tuple_list, k):
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k == 0:
        raise ValueError("k must not be zero")

    if isinstance(tuple_list, (str, bytes, bytearray)):
        raise TypeError("tuple_list must be an iterable of tuples")

    try:
        iterator = iter(tuple_list)
    except TypeError as exc:
        raise TypeError("tuple_list must be an iterable of tuples") from exc

    result = []

    for item in iterator:
        if not isinstance(item, tuple):
            raise TypeError("all items must be tuples")

        all_divisible = True

        for value in item:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("tuple elements must be integers")
            if value % k != 0:
                all_divisible = False

        if all_divisible:
            result.append(item)

    return result
