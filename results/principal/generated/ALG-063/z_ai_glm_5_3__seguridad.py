import math


def max_difference(test_list):
    """Find the maximum difference between available pairs in the given tuple list.

    Each element must be a pair (tuple or list) containing exactly two
    finite numeric values (int or float). Returns the largest absolute
    difference found within any single pair.
    """
    if not isinstance(test_list, (list, tuple)):
        raise TypeError("Input must be a list or tuple of pairs.")

    if len(test_list) == 0:
        raise ValueError("Input must contain at least one pair.")

    max_diff = None

    for index, pair in enumerate(test_list):
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError(
                f"Element at index {index} must be a pair with exactly two values."
            )

        first, second = pair

        for value in (first, second):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    f"Pair at index {index} must contain numeric values."
                )
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError(
                    f"Pair at index {index} must contain finite numbers."
                )

        diff = abs(second - first)
        if max_diff is None or diff > max_diff:
            max_diff = diff

    return max_diff
