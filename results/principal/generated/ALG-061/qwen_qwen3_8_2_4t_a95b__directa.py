def count_substrings(s):
    prefix_counts = {0: 1}
    prefix_sum = 0
    result = 0

    for ch in s:
        prefix_sum += int(ch) - 1
        result += prefix_counts.get(prefix_sum, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return result
