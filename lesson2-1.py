from collections.abc import Callable


def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    stringfield = to_string(file)
    return f"```\n{stringfield}\n```"
