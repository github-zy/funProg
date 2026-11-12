def list_files(
    parent_directory: dict[str, dict | None], current_filepath: str = ""
) -> list[str]:
    list = []
    for key, value in parent_directory.items():
        current_path = current_filepath + "/" + key
        if value is None:
            list.append(current_path)
        else:
            list.extend(list_files(value, current_path))
    return list