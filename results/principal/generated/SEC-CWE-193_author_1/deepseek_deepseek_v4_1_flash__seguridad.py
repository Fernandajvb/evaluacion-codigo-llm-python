def incrementByOne(arr):
    if not isinstance(arr, list):
        raise TypeError("arr must be a list of integers")
    for i, x in enumerate(arr):
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError(f"arr[{i}] must be an integer")
    return [x + 1 for x in arr]
