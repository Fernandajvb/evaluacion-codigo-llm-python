def is_monotonic(arr):
    if len(arr) <= 1:
        return True
    increasing = True
    decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
