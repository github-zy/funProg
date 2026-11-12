def find_longest_word(document: str, longest_word: str = "") -> str:
    if not document:
        return longest_word
    else:
        first_word, rest_of_string = document.split(" ",maxsplit=1)
        if len(first_word) > len(longest_word):
            longest_word = first_word
        if len(rest_of_string) > 0:
            return find_longest_word(rest_of_string, longest_word)
        else:
            return longest_word