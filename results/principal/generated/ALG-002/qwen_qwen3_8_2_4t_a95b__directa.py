def shared_elements(list1, list2):
    set2 = set(list2)
    seen = set()
    result = []
    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            result.append(item)
    return result
