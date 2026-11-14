from collections.abc import Callable


def create_markdown_image(alt_text: str) -> Callable[[str], Callable[..., str]]:
    alt_text = f"![{alt_text}]"
    def with_url(url: str) -> Callable[..., str]:
        url = f"({url.replace('(', '%28').replace(')', '%29')})"
        alt_text_with_url = f"{alt_text}{url}"
        def with_title(title: str = None) -> str:
            image_syntax = alt_text_with_url
            if title is not None:
                title = f"\"{title}\""
                image_syntax = f"{alt_text_with_url[:-1]} {title})"
            return image_syntax
        return with_title
    return with_url
