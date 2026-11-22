def find_shared_elements(list1, list2):
    """
    Find the shared (common) elements between two lists.

    The result contains each shared element exactly once, in the order
    of its first appearance in list1.

    Args:
        list1: First list.
        list2: Second list.

    Returns:
        A list of elements present in both input lists.

    Raises:
        TypeError: If either argument is not a list.
    """
    if not isinstance(list1, list):
        raise TypeError(
            "Expected 'list1' to be a list, got {}.".format(type(list1).__name__)
        )
    if not isinstance(list2, list):
        raise TypeError(
            "Expected 'list2' to be a list, got {}.".format(type(list2).__name__)
        )

    try:
        # Fast path: hash-based lookup, O(len(list1) + len(list2)).
        lookup = set(list2)
        seen = set()
        shared = []
        for item in list1:
            if item in lookup and item not in seen:
                seen.add(item)
                shared.append(item)
        return shared
    except TypeError:
        # Fallback for lists containing unhashable elements
        # (e.g., nested lists or dicts): equality-based search.
        shared = []
        for item in list1:
            if item in list2 and item not in shared:
                shared.append(item)
        return shared
