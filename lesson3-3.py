def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    copy_dict = default_formats.copy()
    copy_dict[new_format] = True
    return copy_dict


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    copy_dict = default_formats.copy()
    copy_dict[old_format] = False
    return copy_dict
