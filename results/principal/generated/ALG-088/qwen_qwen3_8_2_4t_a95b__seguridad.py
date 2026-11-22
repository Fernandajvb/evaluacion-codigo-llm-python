def get_frequency(items: list) -> dict:
    if not isinstance(items, list):
        raise TypeError("items must be a list")

    frequencies = {}

    for index, item in enumerate(items):
        try:
            frequencies[item] = frequencies.get(item, 0) + 1
        except TypeError as exc:
            raise TypeError(f"item at index {index} is not hashable") from exc

    return frequencies
