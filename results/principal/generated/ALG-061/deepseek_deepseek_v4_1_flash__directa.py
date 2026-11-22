def count_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += int(s[j])
            length = j - i + 1
            if total == length:
                count += 1
    return count
