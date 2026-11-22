from numbers import Number


def flatten_and_sum(data):
    """Flatten an arbitrarily nested list and return the sum of all numeric elements."""
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")

    total = 0
    stack = [data]

    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, bool):
                raise TypeError("Boolean values are not valid numeric elements.")
            elif isinstance(item, list):
                stack.append(item)
            elif isinstance(item, Number):
                total += item
            else:
                raise TypeError(
                    "Unsupported element of type "
                    f"'{type(item).__name__}': only numbers and nested lists are allowed."
                )

    return total
