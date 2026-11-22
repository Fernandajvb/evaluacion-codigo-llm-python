from typing import Sequence


def is_substring_in_list(string_list: Sequence[str], substring: str) -> bool:
    """
    Return True if `substring` occurs as a substring in at least one
    element of `string_list` (a list/tuple of string values), otherwise
    return False.

    An empty `substring` is considered a substring of any string,
    following Python's standard semantics, so it yields True for any
    non-empty list of strings and False for an empty list.

    Raises:
        TypeError: if `substring` is not a str, if `string_list` is not a
            list/tuple of strings, or if any element is not a str.
    """
    # Validate the substring argument.
    if not isinstance(substring, str):
        raise TypeError(
            "substring must be a str, got %s" % type(substring).__name__
        )

    # Reject common incorrect argument types (a single string/bytes
    # object is not a list of strings).
    if isinstance(string_list, (str, bytes, bytearray)):
        raise TypeError(
            "string_list must be a list or tuple of strings, not a single %s"
            % type(string_list).__name__
        )

    # Validate that string_list is a supported sequence type.
    if not isinstance(string_list, (list, tuple)):
        raise TypeError(
            "string_list must be a list or tuple of strings, got %s"
            % type(string_list).__name__
        )

    # Validate every element before doing any matching, so invalid data
    # is always reported regardless of where it appears.
    for index, element in enumerate(string_list):
        if not isinstance(element, str):
            raise TypeError(
                "string_list[%d] must be a str, got %s"
                % (index, type(element).__name__)
            )

    # Safe substring check using str.__contains__ (no regex, no eval).
    return any(substring in element for element in string_list)
