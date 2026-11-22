def shared_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")

    try:
        set2 = set(list2)
        seen = set()
        result = []

        for item in list1:
            if item in set2 and item not in seen:
                result.append(item)
                seen.add(item)

        return result
    except TypeError:
        result = []

        for item in list1:
            if any(item == existing for existing in result):
                continue

            if any(item == other for other in list2):
                result.append(item)

        return result
