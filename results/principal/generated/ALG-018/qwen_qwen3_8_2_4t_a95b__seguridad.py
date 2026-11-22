def remove_characters(first_string: str, second_string: str) -> str:
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        raise TypeError("Both arguments must be strings.")

    characters_to_remove = set(second_string)
    return "".join(
        character for character in first_string
        if character not in characters_to_remove
    )
