def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    if not isinstance(password, str):
        return False

    # Longitud mínima: 12 caracteres
    if len(password) < 12:
        return False

    # No se permiten espacios en blanco
    if any(char.isspace() for char in password):
        return False

    # Debe contener al menos una letra mayúscula
    if not any(char.isupper() for char in password):
        return False

    # Debe contener al menos una letra minúscula
    if not any(char.islower() for char in password):
        return False

    # Debe contener al menos un dígito
    if not any(char.isdigit() for char in password):
        return False

    # Debe contener al menos un carácter especial
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/~"
    if not any(char in special_characters for char in password):
        return False

    # No debe contener palabras comunes o predecibles
    lowered = password.lower()
    if "admin" in lowered or "password" in lowered or "1234" in lowered:
        return False

    # No se permiten más de dos caracteres consecutivos repetidos
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    return True
