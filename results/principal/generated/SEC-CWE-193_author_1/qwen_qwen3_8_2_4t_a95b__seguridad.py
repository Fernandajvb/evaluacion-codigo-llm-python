def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    if not isinstance(arr, (list, tuple)):
        raise TypeError("arr must be a list or tuple of integers")

    incremented = []
    for value in arr:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("all elements in arr must be integers")
        incremented.append(value + 1)

    if isinstance(arr, list):
        arr[:] = incremented
        return arr

    return tuple(incremented)
