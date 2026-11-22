def largest_number(digits):
    if not isinstance(digits, list):
        raise TypeError("digits must be a list")

    if not digits:
        raise ValueError("digits must not be empty")

    for digit in digits:
        if isinstance(digit, bool) or not isinstance(digit, int):
            raise TypeError("each digit must be an integer")
        if digit < 0 or digit > 9:
            raise ValueError("each digit must be between 0 and 9")

    result = 0
    for digit in sorted(digits, reverse=True):
        result = result * 10 + digit

    return result
