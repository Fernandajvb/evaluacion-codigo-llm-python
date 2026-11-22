import heapq


def n_largest(nums, n):
    return heapq.nlargest(n, nums)
