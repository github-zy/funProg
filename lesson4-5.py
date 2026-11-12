def sum_nested_list(lst: list[int | list]) -> int:
    total = 0
    for item in list:
        if not isinstance(item, list):
            total += item
        else:
            total += sum_nested_list(item)
    return total
