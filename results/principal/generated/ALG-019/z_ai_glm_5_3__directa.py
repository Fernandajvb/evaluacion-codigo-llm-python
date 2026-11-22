def contains_duplicate(nums):
    """Return True if the given array of integers contains any duplicate element."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
