from collections import defaultdict


def count_substrings_sum_equal_length(digit_string: str) -> int:
    """
    Count the substrings of `digit_string` whose digit sum equals their length.

    A substring s[i..j] qualifies when:
        sum(digits of s[i..j]) == (j - i + 1)

    Runs in O(n) time and O(n) space. Using prefix sums P[k] of digit values,
    the condition for substring (i, j] is:
        P[j] - P[i] == j - i
    which rearranges to:
        (P[j] - j) == (P[i] - i)
    so the answer is the number of index pairs with equal "prefix sum minus index".

    Raises:
        TypeError:  if `digit_string` is not a `str`.
        ValueError: if `digit_string` contains characters outside '0'-'9'.
    """
    if not isinstance(digit_string, str):
        raise TypeError("Input must be a str.")
    if not digit_string:
        return 0
    for ch in digit_string:
        if not ("0" <= ch <= "9"):
            raise ValueError("Input must contain only ASCII digits '0'-'9'.")

    # balance == P[k] - k for the current position k.
    # balance starts at P[0] - 0 == 0 and each digit d shifts it by d - 1,
    # because the digit sum grows by d while the index grows by 1.
    counts = defaultdict(int)
    counts[0] = 1
    balance = 0
    total = 0
    for ch in digit_string:
        balance += (ord(ch) - ord("0")) - 1
        total += counts[balance]
        counts[balance] += 1
    return total


if __name__ == "__main__":
    def _brute_force(s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            acc = 0
            for j in range(i, n):
                acc += ord(s[j]) - ord("0")
                if acc == (j - i + 1):
                    result += 1
        return result

    samples = [
        "",
        "0",
        "123",
        "110",
        "112",
        "99",
        "1001",
        "1111111111",
        "1234",
        "2090",
    ]
    for sample in samples:
        expected = _brute_force(sample)
        got = count_substrings_sum_equal_length(sample)
        assert got == expected, (sample, got, expected)
        print(f"{sample!r}: {got}")

    for bad in (None, 123, ["1", "2"], "12a3", "١٢٣", "12 3", b"123"):
        try:
            count_substrings_sum_equal_length(bad)
        except (TypeError, ValueError):
            print(f"Rejected invalid input: {bad!r}")
        else:
            raise AssertionError(f"Input should have been rejected: {bad!r}")

    print("All checks passed.")
