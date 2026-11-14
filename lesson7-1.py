from collections.abc import Callable


def converted_font_size(doc_type: str) -> Callable[[int], int]:
    def inner(font_size: int) -> int:
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")    
    return inner