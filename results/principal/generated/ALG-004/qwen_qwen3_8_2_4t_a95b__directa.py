import heapq

def find_n_largest_integers(numbers, n):
    if n <= 0:
        return []
    return heapq.nlargest(n, numbers)
