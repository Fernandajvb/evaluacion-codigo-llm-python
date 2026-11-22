def largest_number(digits):
    if not isinstance(digits, (list, tuple)):
        raise TypeError("digits must be a list or tuple")
    if not digits:
        raise ValueError("digits must not be empty")

    for digit in digits:
        if isinstance(digit, bool) or not isinstance(digit, int):
            raise TypeError("each digit must be an integer")
        if digit < 0 or digit > 9:
            raise ValueError("each digit must be between 0 and 9")

    ordered = sorted(digits, reverse=True)
    return int("".join(str(digit) for digit in ordered))
