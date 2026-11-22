def largest_number(digits):
    if not digits:
        return 0
    return int(''.join(map(str, sorted(digits, reverse=True))))
