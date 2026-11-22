def get_Char(input_string):
    """
    Devuelve el caracter obtenido al sumar los valores ASCII de todos los
    caracteres de la cadena dada y aplicar modulo 26.

    El residuo se mapea a una letra minuscula:
        1 -> 'a', 2 -> 'b', ..., 25 -> 'y', 0 -> 'z'
    """
    # Validación de entrada: debe ser una cadena no vacía.
    if not isinstance(input_string, str):
        raise TypeError("La entrada debe ser una cadena de texto (str).")
    if not input_string:
        raise ValueError("La cadena de entrada no puede estar vacía.")

    total = sum(ord(char) for char in input_string)
    remainder = total % 26

    if remainder == 0:
        return 'z'
    return chr(96 + remainder)
