def is_monotonic(arr) -> bool:
    if arr is None:
        raise ValueError("Input array must not be None.")

    try:
        iterator = iter(arr)
    except TypeError as exc:
        raise TypeError("Input must be an iterable.") from exc

    try:
        previous = next(iterator)
    except StopIteration:
        return True

    non_decreasing = True
    non_increasing = True

    for current in iterator:
        try:
            if current < previous:
                non_decreasing = False
            elif current > previous:
                non_increasing = False
            elif current != previous:
                return False
        except (TypeError, ValueError) as exc:
            raise TypeError("Array elements must be comparable.") from exc

        if not non_decreasing and not non_increasing:
            return False

        previous = current

    return True
