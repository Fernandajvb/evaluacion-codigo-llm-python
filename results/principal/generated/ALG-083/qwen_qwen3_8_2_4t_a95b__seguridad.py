def find_character(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("La entrada debe ser una cadena de texto")

    try:
        ascii_values = s.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("La entrada debe contener únicamente caracteres ASCII") from exc

    return chr((sum(ascii_values) % 26) + ord("A"))
