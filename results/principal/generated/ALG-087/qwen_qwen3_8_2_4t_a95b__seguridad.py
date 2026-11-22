from collections.abc import Mapping

def merge_three_dicts(first, second, third):
    if not all(isinstance(item, Mapping) for item in (first, second, third)):
        raise TypeError("All arguments must be dictionaries or dictionary-like mappings.")

    merged = {}
    merged.update(first)
    merged.update(second)
    merged.update(third)
    return merged
