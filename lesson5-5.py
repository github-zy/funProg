from collections.abc import Callable


def get_filter_cmd(
    filter_one: Callable[[str], str], filter_two: Callable[[str], str]
) -> Callable[[str, str], str]:
    def filter_cmd(content: str, option: str = "--one") -> str:
        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option == "--three":
            return filter_two(filter_one(content))
        else:
            raise ValueError(f"Invalid option: {option}")

    return filter_cmd


# Don't touch below this line


def replace_bad(text: str) -> str:
    return text.replace("bad", "good")


def replace_ellipsis(text: str) -> str:
    return text.replace("..", "...")


def fix_ellipsis(text: str) -> str:
    return text.replace("....", "...")
