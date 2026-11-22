def differ_at_one_bit_position(a: int, b: int) -> bool:
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Both inputs must be integers, not booleans")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Both integers must be non-negative")

    xor = a ^ b
    return xor != 0 and (xor & (xor - 1)) == 0
