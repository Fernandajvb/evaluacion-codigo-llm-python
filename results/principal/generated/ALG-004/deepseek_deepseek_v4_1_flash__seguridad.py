import heapq

def n_largest(numbers, n):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    for value in numbers:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("all elements must be integers")
    return heapq.nlargest(n, numbers)
