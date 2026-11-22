def largest_number_from_digits(digits):
    """
    Build the largest possible number by arranging the provided digits.

    Args:
        digits: A list or tuple of integers, each in the range 0-9.

    Returns:
        int: The largest number that can be formed from the digits.

    Raises:
        TypeError: If `digits` is not a list/tuple or contains non-integer items.
        ValueError: If `digits` is empty or contains values outside 0-9.
    """
    if not isinstance(digits, (list, tuple)):
        raise TypeError("digits must be a list or tuple of integers")

    if len(digits) == 0:
        raise ValueError("digits must contain at least one digit")

    validated = []
    for value in digits:
        # bool is a subclass of int in Python, so reject it explicitly.
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                "all elements must be integers, got {!r}".format(type(value).__name__)
            )
        if not 0 <= value <= 9:
            raise ValueError(
                "each digit must be in the range 0-9, got {!r}".format(value)
            )
        validated.append(value)

    # Arrange digits in descending order and build the number arithmetically
    # (avoids string conversion and preserves leading-zero collapse, e.g. [0, 0] -> 0).
    largest = 0
    for digit in sorted(validated, reverse=True):
        largest = largest * 10 + digit

    return largest


if __name__ == "__main__":
    assert largest_number_from_digits([1, 2, 3]) == 321
    assert largest_number_from_digits([5, 0, 9, 5]) == 9550
    assert largest_number_from_digits([0, 0]) == 0
    assert largest_number_from_digits([7]) == 7
    assert largest_number_from_digits([3, 1, 4, 1, 5, 9, 2, 6]) == 96543321

    try:
        largest_number_from_digits("123")
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError for non-list/tuple input")

    try:
        largest_number_from_digits([])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for empty input")

    try:
        largest_number_from_digits([1, 12])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for out-of-range digit")

    try:
        largest_number_from_digits([1, True])
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError for boolean element")

    print("All tests passed.")
