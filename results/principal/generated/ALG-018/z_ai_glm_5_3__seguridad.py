def remove_chars(str1, str2):
    """
    Remove from str1 every character that is present in str2.

    Args:
        str1: Source string from which characters will be removed.
        str2: String containing the characters to remove.

    Returns:
        A new string with all matching characters removed.

    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(str1, str):
        raise TypeError(
            "str1 must be a str, got {}".format(type(str1).__name__)
        )
    if not isinstance(str2, str):
        raise TypeError(
            "str2 must be a str, got {}".format(type(str2).__name__)
        )

    chars_to_remove = set(str2)
    return "".join(ch for ch in str1 if ch not in chars_to_remove)


if __name__ == "__main__":
    assert remove_chars("hello world", "lo") == "he wrd"
    assert remove_chars("python", "") == "python"
    assert remove_chars("", "abc") == ""
    assert remove_chars("aabbcc", "abc") == ""
    assert remove_chars("aeiou", "aeiou") == ""
    print("All tests passed.")
