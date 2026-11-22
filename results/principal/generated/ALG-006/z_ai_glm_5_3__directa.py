def differ_At_One_Bit_Pos(x, y):
    diff = x ^ y
    return diff != 0 and (diff & (diff - 1)) == 0
