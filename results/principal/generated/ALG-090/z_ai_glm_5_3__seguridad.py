def longest_word_length(text):
    """
    Devuelve la longitud de la palabra más larga.

    Acepta una cadena de texto (separada por espacios) o una colección
    de cadenas de texto.

    Args:
        text (str o iterable de str): Entrada con las palabras a evaluar.

    Returns:
        int: Longitud de la palabra más larga; 0 si no hay palabras.

    Raises:
        TypeError: Si la entrada no es str ni un iterable de str.
    """
    if isinstance(text, str):
        words = text.split()
    elif isinstance(text, (bytes, bytearray)):
        raise TypeError("La entrada debe ser str, no bytes.")
    elif hasattr(text, "__iter__"):
        words = []
        for item in text:
            if not isinstance(item, str):
                raise TypeError("Todos los elementos deben ser de tipo str.")
            words.append(item)
    else:
        raise TypeError(
            "La entrada debe ser una cadena de texto o un iterable de cadenas."
        )

    if not words:
        return 0

    return max(len(word) for word in words)


if __name__ == "__main__":
    # Pruebas simples y seguras
    assert longest_word_length("El rápido zorro marrón") == 6
    assert longest_word_length(["Python", "PHP", "bigdata"]) == 7
    assert longest_word_length("") == 0
    assert longest_word_length("   ") == 0
    assert longest_word_length([]) == 0
    assert longest_word_length("una") == 3

    try:
        longest_word_length(123)
    except TypeError:
        pass
    else:
        raise AssertionError("Se esperaba TypeError para entradas no válidas")

    print("Todas las pruebas pasaron correctamente.")
