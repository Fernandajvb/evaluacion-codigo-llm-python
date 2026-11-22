def max_sum_list(lists):
    if not isinstance(lists, list):
        raise TypeError("Input must be a list of lists")
    if not lists:
        raise ValueError("Input list cannot be empty")
    for i, sublist in enumerate(lists):
        if not isinstance(sublist, list):
            raise TypeError(f"Element at index {i} is not a list")
    return max(lists, key=sum)
