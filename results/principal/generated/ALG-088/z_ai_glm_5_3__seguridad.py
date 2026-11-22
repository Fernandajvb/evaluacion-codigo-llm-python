from typing import Any, Dict, Hashable, List


def get_frequency(items: List[Any]) -> Dict[Hashable, int]:
    """Return a dictionary mapping each element of `items` to its frequency.

    Args:
        items: A list whose elements must be hashable.

    Returns:
        A dictionary where keys are the distinct elements of `items`
        and values are the number of times each element appears.

    Raises:
        TypeError: If `items` is not a list, or if it contains an
            unhashable element (which cannot be a dictionary key).
    """
    if not isinstance(items, list):
        raise TypeError(
            f"Expected a list, got {type(items).__name__}"
        )

    frequencies: Dict[Hashable, int] = {}
    for index, element in enumerate(items):
        try:
            hash(element)
        except TypeError as exc:
            raise TypeError(
                f"Element at index {index} ({element!r}) is not hashable "
                "and cannot be used as a dictionary key."
            ) from exc
        frequencies[element] = frequencies.get(element, 0) + 1

    return frequencies
