def max_sum_list(list_of_lists):
    if not list_of_lists:
        return None
    return max(list_of_lists, key=sum)
