def validate_password(actual_pw, typed_pw):
    return len(actual_pw) == len(typed_pw) and all(a == b for a, b in zip(actual_pw, typed_pw))
