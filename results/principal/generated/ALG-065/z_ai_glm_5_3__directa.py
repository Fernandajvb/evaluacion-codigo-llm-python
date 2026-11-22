def flatten_and_sum(nested_list):
    def flatten(lst):
        flat = []
        for item in lst:
            if isinstance(item, list):
                flat.extend(flatten(item))
            else:
                flat.append(item)
        return flat
    return sum(flatten(nested_list))
