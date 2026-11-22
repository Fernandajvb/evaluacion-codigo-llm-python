def shared_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")
    try:
        set2 = set(list2)
        seen = set()
        result = []
        for item in list1:
            if item in set2 and item not in seen:
                seen.add(item)
                result.append(item)
        return result
    except TypeError:
        result = []
        for item in list1:
            if item in list2 and item not in result:
                result.append(item)
        return result
