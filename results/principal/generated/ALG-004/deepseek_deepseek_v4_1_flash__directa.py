def n_largest(numbers, n):
    if n <= 0:
        return []
    return sorted(numbers, reverse=True)[:n]
