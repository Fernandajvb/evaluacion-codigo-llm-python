def merge_three_dicts(dict1, dict2, dict3):
    if not all(isinstance(d, dict) for d in (dict1, dict2, dict3)):
        raise TypeError("All arguments must be dictionaries")
    merged = {}
    merged.update(dict1)
    merged.update(dict2)
    merged.update(dict3)
    return merged
