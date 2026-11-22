def is_monotonic(array):
    if array is None:
        raise ValueError("array must not be None")
    try:
        items = list(array)
    except TypeError as exc:
        raise TypeError("array must be iterable") from exc

    if len(items) <= 2:
        return True

    increasing = True
    decreasing = True

    for i in range(1, len(items)):
        if items[i] < items[i - 1]:
            increasing = False
        if items[i] > items[i - 1]:
            decreasing = False
        if not increasing and not decreasing:
            return False

    return True
