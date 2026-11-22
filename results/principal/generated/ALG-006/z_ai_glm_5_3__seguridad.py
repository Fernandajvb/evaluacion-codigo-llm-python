def differ_at_one_bit_position(num1, num2):
    """Return True if num1 and num2 differ at exactly one bit position.

    Two non-negative integers differ at exactly one bit position if and
    only if their XOR results in a non-zero power of two (a single set bit).
    """
    for name, value in (("num1", num1), ("num2", num2)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                f"{name} must be an integer, got {type(value).__name__}"
            )
        if value < 0:
            raise ValueError(f"{name} must be a non-negative integer, got {value}")

    diff = num1 ^ num2
    # A value has exactly one bit set iff it is non-zero and a power of two.
    return diff != 0 and (diff & (diff - 1)) == 0


if __name__ == "__main__":
    # Basic sanity checks (self-contained, safe to run directly).
    assert differ_at_one_bit_position(13, 9) is True    # 1101 vs 1001 -> differ at bit 2
    assert differ_at_one_bit_position(0, 1) is True     # 0000 vs 0001 -> differ at bit 0
    assert differ_at_one_bit_position(13, 14) is False  # 1101 vs 1110 -> differ at bits 0 and 3
    assert differ_at_one_bit_position(7, 7) is False    # identical -> differ at zero positions
    assert differ_at_one_bit_position(1, 4) is False   # 001 vs 100 -> differ at bits 0 and 2

    # Validation checks.
    for bad_args in ((13, 9.0), ("13", 9), (True, 2), (-1, 2)):
        try:
            differ_at_one_bit_position(*bad_args)
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError(f"Expected validation error for {bad_args!r}")

    print("All checks passed.")
