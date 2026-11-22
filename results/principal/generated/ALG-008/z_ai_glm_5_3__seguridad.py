def square_elements(values):
    """Return a new list with the square of each numeric element in `values`.

    Args:
        values: A list whose elements are int or float (bools are rejected).

    Returns:
        A list containing the square of each element, in the same order.

    Raises:
        TypeError: If `values` is not a list, or if any element is not an
            int or float.
    """
    if not isinstance(values, list):
        raise TypeError(
            f"Expected a list, got {type(values).__name__}."
        )

    squared = []
    for index, element in enumerate(values):
        # bool is a subclass of int; reject it explicitly to avoid surprises.
        if isinstance(element, bool) or not isinstance(element, (int, float)):
            raise TypeError(
                f"Element at index {index} must be an int or float, "
                f"got {type(element).__name__} ({element!r})."
            )
        squared.append(element * element)

    return squared
