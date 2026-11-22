def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    '''
    if len(actual_pw) != len(typed_pw):
        return False

    for actual_char, typed_char in zip(actual_pw, typed_pw):
        if actual_char != typed_char:
            return False

    return True
