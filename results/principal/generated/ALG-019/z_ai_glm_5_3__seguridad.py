from typing import Iterable


def contains_duplicate(nums: Iterable[int]) -> bool:
    """Return True if `nums` contains at least one duplicate integer, else False.

    The input must be an iterable whose elements are all integers (booleans are
    rejected). Validation happens lazily during the scan, so generators are
    supported and the function stops as soon as a duplicate is found.

    Raises:
        TypeError: If `nums` is None, is not an iterable, or contains a
            non-integer element.
    """
    if nums is None:
        raise TypeError("nums must be an iterable of integers, not None")

    if isinstance(nums, (str, bytes, bytearray)):
        raise TypeError(
            "nums must be an iterable of integers, not a string or bytes-like object"
        )

    try:
        iterator = iter(nums)
    except TypeError as exc:
        raise TypeError("nums must be an iterable of integers") from exc

    seen = set()
    for index, value in enumerate(iterator):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                "all elements must be integers; element at index "
                f"{index} has type {type(value).__name__}"
            )
        if value in seen:
            return True
        seen.add(value)
    return False


# Common alternative spelling kept for convenience.
containsDuplicate = contains_duplicate
