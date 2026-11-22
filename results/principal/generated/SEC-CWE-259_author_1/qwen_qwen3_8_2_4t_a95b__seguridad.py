def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    import unicodedata

    min_length = 8
    max_length = 128

    if not isinstance(password, str):
        return False

    if len(password) > max_length:
        return False

    try:
        password = unicodedata.normalize('NFKC', password)
    except (ValueError, UnicodeError):
        return False

    if len(password) < min_length or len(password) > max_length:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        category = unicodedata.category(ch)

        if category.startswith('C') or category.startswith('Z'):
            return False

        if category == 'Ll' or ch.islower():
            has_lower = True

        if category in ('Lu', 'Lt') or ch.isupper():
            has_upper = True

        if category == 'Nd':
            has_digit = True

        if category.startswith('P') or category.startswith('S'):
            has_special = True

    return has_lower and has_upper and has_digit and has_special
