from collections.abc import Callable


def new_collection(initial_docs: list[str]) -> Callable[[str], list[str]]:
    docs: list[str] = initial_docs.copy()
    def add_doc(doc: str) -> list[str]:
        docs.append(doc)
        return docs
    return add_doc