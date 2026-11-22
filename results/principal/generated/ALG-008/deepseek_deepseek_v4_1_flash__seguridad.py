from numbers import Number

def square_elements(values):
    if not isinstance(values, list):
        raise TypeError("Input must be a list")
    for value in values:
        if not isinstance(value, Number):
            raise TypeError("All elements must be numbers")
    return [value * value for value in values]
