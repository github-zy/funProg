from collections.abc import Callable


def word_count_aggregator() -> Callable[[str], int]:
    count: int = 0

    def word_count(document: str) -> int:
        nonlocal count
        count += len(document.split())
        return count
    return word_count