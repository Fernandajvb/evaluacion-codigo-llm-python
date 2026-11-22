def max_sum_list(lists):
    if not lists:
        return None
    return max(lists, key=sum)
