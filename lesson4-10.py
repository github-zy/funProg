def count_nested_levels(
    nested_documents: dict[int, dict], target_document_id: int, level: int = 1
) -> int:
    for document_id, document in nested_documents.items():
        if document_id == target_document_id:
            return level
        if isinstance(document, dict):
            nested_level = count_nested_levels(document, target_document_id, level + 1)
            if nested_level != -1:
                return nested_level
    return -1
