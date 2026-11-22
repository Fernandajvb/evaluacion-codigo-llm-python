def square_elements(elements):
    if not isinstance(elements, list):
        raise TypeError("elements must be a list")

    squares = []
    for item in elements:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise TypeError("all elements must be integers or floats")
        squares.append(item * item)

    return squares
