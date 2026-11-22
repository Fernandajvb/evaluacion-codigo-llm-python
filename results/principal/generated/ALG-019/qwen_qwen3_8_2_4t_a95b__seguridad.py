def contains_duplicate(arr):
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or tuple of integers.")

    seen = set()
    for value in arr:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("All elements must be integers.")
        if value in seen:
            return True
        seen.add(value)

    return False
