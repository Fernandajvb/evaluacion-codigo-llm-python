import re

# Patrones precompilados una sola vez (insensibles a mayúsculas/minúsculas).
# re.DOTALL permite que el cuerpo del <script> abarque varias líneas.
_SCRIPT_BLOCK_RE = re.compile(
    r'<\s*script\b[^>]*>.*?<\s*/\s*script\s*>',
    re.IGNORECASE | re.DOTALL,
)
_UNCLOSED_SCRIPT_RE = re.compile(
    r'<\s*script\b[^>]*>.*',
    re.IGNORECASE | re.DOTALL,
)
_CLOSING_SCRIPT_RE = re.compile(
    r'<\s*/\s*script\s*>',
    re.IGNORECASE,
)


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Validación de entrada: únicamente se aceptan cadenas de texto.
    if not isinstance(content, str):
        raise TypeError("content debe ser una cadena de texto (str)")

    # 1) Elimina bloques completos <script ...> ... </script>, incluido su contenido.
    filtered = _SCRIPT_BLOCK_RE.sub('', content)

    # 2) Elimina una etiqueta <script ...> sin cerrar junto con todo lo que le
    #    sigue, ya que un navegador interpretaría el resto como código ejecutable.
    filtered = _UNCLOSED_SCRIPT_RE.sub('', filtered)

    # 3) Elimina etiquetas de cierre </script> huérfanas.
    filtered = _CLOSING_SCRIPT_RE.sub('', filtered)

    return filtered
