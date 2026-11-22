def get_frequency(elements):
    if not isinstance(elements, list):
        raise TypeError("elements must be a list")

    frequencies = {}
    for item in elements:
        try:
            hash(item)
        except TypeError as exc:
            raise TypeError("all elements must be hashable") from exc
        frequencies[item] = frequencies.get(item, 0) + 1

    return frequencies
