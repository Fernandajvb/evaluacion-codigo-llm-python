def contains_duplicate(nums):
    if not isinstance(nums, (list, tuple)):
        raise TypeError("nums must be a list or tuple of integers")
    seen = set()
    for value in nums:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("All elements must be integers")
        if value in seen:
            return True
        seen.add(value)
    return False
