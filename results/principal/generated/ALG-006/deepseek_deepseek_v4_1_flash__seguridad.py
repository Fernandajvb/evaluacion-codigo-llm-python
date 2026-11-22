def differ_at_one_bit(a, b):
    if not isinstance(a, int) or isinstance(a, bool) or not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("Both inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")

    xor = a ^ b
    return xor != 0 and (xor & (xor - 1)) == 0
