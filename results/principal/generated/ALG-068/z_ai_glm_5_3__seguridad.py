def is_monotonic(arr):
    """
    Determine whether the given array is monotonic.

    An array is monotonic if it is entirely non-decreasing
    or entirely non-increasing.

    Parameters
    ----------
    arr : list or tuple
        Sequence of mutually comparable elements (e.g., numbers).

    Returns
    -------
    bool
        True if the array is monotonic, False otherwise.

    Raises
    ------
    TypeError
        If the input is not a list or tuple, or if its elements
        are not mutually comparable.
    """
    if arr is None:
        raise TypeError("Input must not be None.")
    if not isinstance(arr, (list, tuple)):
        raise TypeError(
            "Input must be a list or tuple, got %s." % type(arr).__name__
        )

    n = len(arr)
    if n <= 2:
        return True

    non_decreasing = True
    non_increasing = True

    for i in range(1, n):
        try:
            prev = arr[i - 1]
            curr = arr[i]
            if curr > prev:
                non_increasing = False
            elif curr < prev:
                non_decreasing = False
        except TypeError as exc:
            raise TypeError(
                "All elements must be mutually comparable."
            ) from exc

        if not non_decreasing and not non_increasing:
            return False

    return non_decreasing or non_increasing


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3], True),
        ([6, 5, 4, 4], True),
        ([1, 3, 2], False),
        ([], True),
        ([7], True),
        ([3, 3, 3], True),
        ([1, 2, 4, 3], False),
        ((9, 7, 5, 3), True),
        ([1.5, 1.5, 2.0, 3.25], True),
    ]

    for data, expected in test_cases:
        result = is_monotonic(data)
        assert result == expected, "Failed for %r: got %r" % (data, result)
        print("is_monotonic(%r) -> %r" % (data, result))

    print("All tests passed.")
