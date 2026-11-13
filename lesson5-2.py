from collections.abc import Callable


def doc_format_checker_and_converter(
    conversion_function: Callable[[str], str], valid_formats: list[str]
) -> Callable[[str, str], str]:
    def conversion_function_wrapper(filename: str, content: str) -> str:
        name, ext = filename.split(".")
        if not ext in valid_formats:
            raise ValueError(f"Invalid file format: {ext}")
        return conversion_function(content)


# Don't edit below this line


def capitalize_content(content: str) -> str:
    return content.upper()


def reverse_content(content: str) -> str:
    return content[::-1]
