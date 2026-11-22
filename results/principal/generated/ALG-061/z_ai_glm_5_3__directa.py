def count_substrings(s) -> int:
    s = str(s)
    count = 0
    freq = {0: 1}
    prefix_sum = 0
    for i, ch in enumerate(s):
        prefix_sum += int(ch) if ch.isdigit() else 0
        key = prefix_sum - (i + 1)
        count += freq.get(key, 0)
        freq[key] = freq.get(key, 0) + 1
    return count
