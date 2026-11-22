def longest_word_length(text):
    """
    Devuelve la longitud de la palabra más larga.

    Acepta una oración (str) o un iterable de palabras (lista/tupla).
    Devuelve 0 si no hay palabras.
    """
    if isinstance(text, str):
        words = text.split()
    else:
        words = list(text)

    if not words:
        return 0

    return max(len(word) for word in words)


def len_log(list1):
    """
    Alias compatible: recibe una lista de palabras y devuelve
    la longitud de la palabra más larga.
    """
    return longest_word_length(list1)
