import hmac

def validate_password(actual_pw, typed_pw):
    if not isinstance(actual_pw, str) or not isinstance(typed_pw, str):
        raise TypeError("Passwords must be strings")
    return hmac.compare_digest(actual_pw.encode("utf-8"), typed_pw.encode("utf-8"))
