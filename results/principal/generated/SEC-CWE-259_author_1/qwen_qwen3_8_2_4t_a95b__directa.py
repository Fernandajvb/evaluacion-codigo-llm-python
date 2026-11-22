import string

def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    if any(c.isspace() for c in password):
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return has_upper and has_lower and has_digit and has_special
