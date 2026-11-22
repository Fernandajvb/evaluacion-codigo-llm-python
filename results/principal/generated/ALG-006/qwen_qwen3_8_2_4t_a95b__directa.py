def is_one_bit_difference(a, b):
    x = a ^ b
    return x != 0 and (x & (x - 1)) == 0
