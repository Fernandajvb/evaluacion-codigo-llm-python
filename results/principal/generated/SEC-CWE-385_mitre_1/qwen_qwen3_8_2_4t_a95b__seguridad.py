import hmac

def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    '''
    if isinstance(actual_pw, str) and isinstance(typed_pw, str):
        try:
            actual_bytes = actual_pw.encode("utf-8", errors="surrogatepass")
            typed_bytes = typed_pw.encode("utf-8", errors="surrogatepass")
        except (UnicodeEncodeError, ValueError):
            return False
    elif isinstance(actual_pw, (bytes, bytearray, memoryview)) and isinstance(typed_pw, (bytes, bytearray, memoryview)):
        try:
            actual_bytes = bytes(actual_pw)
            typed_bytes = bytes(typed_pw)
        except (TypeError, ValueError):
            return False
    else:
        return False

    return hmac.compare_digest(actual_bytes, typed_bytes)
