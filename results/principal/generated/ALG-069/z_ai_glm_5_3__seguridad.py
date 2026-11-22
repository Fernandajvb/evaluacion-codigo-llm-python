def is_sublist(main_list, sublist):
    """Return True if `sublist` occurs as a contiguous subsequence of `main_list`.

    An empty `sublist` is considered contained in any list.
    Raises TypeError if either argument is not a list or tuple.
    """
    if not isinstance(main_list, (list, tuple)):
        raise TypeError(
            "main_list must be a list or tuple, got %s" % type(main_list).__name__
        )
    if not isinstance(sublist, (list, tuple)):
        raise TypeError(
            "sublist must be a list or tuple, got %s" % type(sublist).__name__
        )

    main_seq = list(main_list)
    sub_seq = list(sublist)

    n = len(main_seq)
    m = len(sub_seq)

    if m == 0:
        return True
    if m > n:
        return False

    for i in range(n - m + 1):
        if main_seq[i] == sub_seq[0] and main_seq[i:i + m] == sub_seq:
            return True
    return False
