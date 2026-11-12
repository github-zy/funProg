def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    if not keys or not values:
        return {}
    else:
        dict = zipmap(keys[1:], values[1:])
        dict[keys[0]] = values[0]
        return dict