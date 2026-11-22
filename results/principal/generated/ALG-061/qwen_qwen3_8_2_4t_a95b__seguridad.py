def count_substrings(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    total = 0
    prefix = 0
    frequencies = {0: 1}

    for character in s:
        if character < "0" or character > "9":
            raise ValueError("Input must contain only ASCII digits.")

        prefix += ord(character) - 49
        previous = frequencies.get(prefix, 0)
        total += previous
        frequencies[prefix] = previous + 1

    return total
