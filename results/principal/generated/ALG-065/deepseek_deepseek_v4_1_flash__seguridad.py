from numbers import Real

def flatten_and_sum(nested_list):
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list.")
    total = 0
    stack = list(nested_list)
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        elif isinstance(item, bool) or not isinstance(item, Real):
            raise TypeError("All elements must be real numbers.")
        else:
            total += item
    return total
