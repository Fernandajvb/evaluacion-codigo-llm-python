def largest_number(digits):
    if not digits:
        return 0
    return int(''.join(sorted(map(str, digits), reverse=True)))
