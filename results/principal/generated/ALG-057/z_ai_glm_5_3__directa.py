def find_Max_Num(arr):
    arr = sorted(arr, reverse=True)
    num = 0
    for d in arr:
        num = num * 10 + d
    return num
