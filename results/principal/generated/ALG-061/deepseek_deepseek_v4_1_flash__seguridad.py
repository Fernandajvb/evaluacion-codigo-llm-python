from collections import defaultdict

def count_substrings_with_sum_equal_length(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    freq = defaultdict(int)
    freq[0] = 1
    prefix = 0
    count = 0
    for ch in s:
        if ch < '0' or ch > '9':
            raise ValueError("Input string must contain only digits")
        prefix += ord(ch) - ord('0') - 1
        count += freq[prefix]
        freq[prefix] += 1
    return count
