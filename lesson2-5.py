def remove_invalid_lines(document: str) -> str:
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )
