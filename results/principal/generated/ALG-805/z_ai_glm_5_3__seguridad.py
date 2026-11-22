import math
from typing import Sequence, Union

Number = Union[int, float]


def highest_sum_list(lists: Sequence[Sequence[Number]]) -> Sequence[Number]:
    """Return the inner list whose elements add up to the highest sum.

    In case of ties, the first list with the highest sum is returned.

    Raises:
        TypeError: If the input is not a sequence of sequences of numbers.
        ValueError: If the input is empty or contains non-finite values.
    """
    if isinstance(lists, (str, bytes)) or not isinstance(lists, (list, tuple)):
        raise TypeError("Input must be a list of lists (or tuples).")
    if len(lists) == 0:
        raise ValueError("Input must contain at least one list.")

    best_list = None
    best_sum = None

    for i, inner in enumerate(lists):
        if isinstance(inner, (str, bytes)) or not isinstance(inner, (list, tuple)):
            raise TypeError(
                f"Element at index {i} must be a list or tuple of numbers."
            )
        current_sum = 0
        for j, value in enumerate(inner):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    f"Value at index {j} of list {i} must be an int or a float."
                )
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError(
                    f"Value at index {j} of list {i} is not finite (NaN or infinity)."
                )
            current_sum += value
        if best_sum is None or current_sum > best_sum:
            best_sum = current_sum
            best_list = inner

    return best_list
