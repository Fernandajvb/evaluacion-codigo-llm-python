from numbers import Number


def flatten_and_sum(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    total = 0
    active = {id(lst)}
    stack = [(iter(lst), id(lst))]

    while stack:
        iterator, container_id = stack[-1]
        try:
            item = next(iterator)
        except StopIteration:
            stack.pop()
            active.discard(container_id)
            continue

        if isinstance(item, list):
            item_id = id(item)
            if item_id in active:
                raise ValueError("Input list contains a cyclic reference.")
            active.add(item_id)
            stack.append((iter(item), item_id))
        elif isinstance(item, bool) or not isinstance(item, Number):
            raise TypeError("All list elements must be numeric.")
        else:
            try:
                total += item
            except TypeError as exc:
                raise TypeError("All list elements must be addable numeric values.") from exc

    return total
