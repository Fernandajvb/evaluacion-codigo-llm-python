from collections.abc import Mapping
from typing import Any


def merge_three_dicts(
    dict1: Mapping[str, Any],
    dict2: Mapping[str, Any],
    dict3: Mapping[str, Any],
) -> dict:
    """Merge three dictionaries into a single new dictionary.

    If a key appears in more than one dictionary, the value from the
    dictionary passed later takes precedence.

    Args:
        dict1: First dictionary (or mapping) to merge.
        dict2: Second dictionary; its keys override dict1's on conflicts.
        dict3: Third dictionary; its keys override the previous ones.

    Returns:
        A new dictionary with the combined key-value pairs. The input
        dictionaries are not modified.

    Raises:
        TypeError: If any argument is not a dictionary or mapping.
    """
    for name, value in (("dict1", dict1), ("dict2", dict2), ("dict3", dict3)):
        if not isinstance(value, Mapping):
            raise TypeError(
                f"'{name}' must be a dict or mapping, got {type(value).__name__}"
            )

    return {**dict1, **dict2, **dict3}


if __name__ == "__main__":
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    d3 = {"d": 5}

    merged = merge_three_dicts(d1, d2, d3)
    print(merged)  # {'a': 1, 'b': 3, 'c': 4, 'd': 5}

    try:
        merge_three_dicts(d1, ["not", "a", "dict"], d3)
    except TypeError as exc:
        print(f"Input validation error: {exc}")
