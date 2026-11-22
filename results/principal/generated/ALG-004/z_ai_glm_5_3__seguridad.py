import heapq
from numbers import Real


def n_largest(numbers, n):
    """Return the n largest numbers from `numbers` in descending order.

    Args:
        numbers: An iterable of real numbers (e.g., list of ints/floats).
        n: A non-negative integer specifying how many values to return.

    Returns:
        A list containing the n largest values, sorted in descending order.

    Raises:
        TypeError: If `numbers` is not an iterable of real numbers, or if
            `n` is not an integer.
        ValueError: If `n` is negative, exceeds the number of available
            elements, or if the input contains NaN values.
    """
    if isinstance(numbers, (str, bytes, bytearray)) or not hasattr(numbers, "__iter__"):
        raise TypeError("numbers must be an iterable of numeric values")

    items = list(numbers)

    for index, value in enumerate(items):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(
                "all elements must be real numbers; "
                f"found {type(value).__name__} at index {index}"
            )
        if isinstance(value, float) and value != value:
            raise ValueError(f"NaN values are not allowed; found at index {index}")

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n > len(items):
        raise ValueError(
            f"n ({n}) cannot exceed the number of available elements ({len(items)})"
        )

    if n == 0:
        return []

    return heapq.nlargest(n, items)
