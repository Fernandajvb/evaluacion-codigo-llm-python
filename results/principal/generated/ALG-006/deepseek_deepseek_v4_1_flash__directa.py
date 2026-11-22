def differ_at_one_bit(a, b):
    x = a ^ b
    return x != 0 and (x & (x - 1)) == 0
