def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    if not isinstance(arr, list):
        raise TypeError("arr must be a list of integers")

    for index, element in enumerate(arr):
        if isinstance(element, bool) or not isinstance(element, int):
            raise ValueError(
                "Element at index {} must be an integer, got {}".format(
                    index, type(element).__name__
                )
            )

    for index in range(len(arr)):
        arr[index] += 1

    return arr
