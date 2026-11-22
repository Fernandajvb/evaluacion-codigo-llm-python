import hmac

_MAX_PASSWORD_BYTES = 4096  # Sane upper bound; limits comparison work per call.


def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    '''
    # --- Input validation: only text or bytes-like values are comparable. ---
    if isinstance(actual_pw, str):
        actual_is_text = True
    elif isinstance(actual_pw, (bytes, bytearray)):
        actual_is_text = False
    else:
        raise TypeError(
            "actual_pw must be a str or bytes-like object, not "
            + type(actual_pw).__name__
        )

    if isinstance(typed_pw, str):
        typed_is_text = True
    elif isinstance(typed_pw, (bytes, bytearray)):
        typed_is_text = False
    else:
        raise TypeError(
            "typed_pw must be a str or bytes-like object, not "
            + type(typed_pw).__name__
        )

    if actual_is_text != typed_is_text:
        raise TypeError(
            "actual_pw and typed_pw must both be str or both bytes-like"
        )

    # Normalize to bytes so the comparison is well defined and independent of
    # Unicode representation details. UTF-8 is injective, so byte equality is
    # equivalent to character-by-character equality.
    try:
        actual_bytes = actual_pw.encode("utf-8") if actual_is_text else bytes(actual_pw)
        typed_bytes = typed_pw.encode("utf-8") if typed_is_text else bytes(typed_pw)
    except UnicodeEncodeError:
        # Unencodable text (e.g., lone surrogates) can never equal a valid
        # stored password; fail closed without leaking content details.
        return False

    if len(actual_bytes) > _MAX_PASSWORD_BYTES or len(typed_bytes) > _MAX_PASSWORD_BYTES:
        raise ValueError("password exceeds the maximum supported length")

    # --- Secure comparison ---
    # Primary check: hmac.compare_digest inspects every byte in constant time
    # (no early exit), so neither the result nor its timing reveals where a
    # mismatch occurred. This mitigates timing attacks on password checks.
    constant_time_match = hmac.compare_digest(actual_bytes, typed_bytes)

    # Defense in depth: explicit per-character check with no short-circuit,
    # so every position is examined regardless of earlier mismatches.
    n = max(len(actual_bytes), len(typed_bytes))
    mismatch = 0
    for i in range(n):
        ca = actual_bytes[i] if i < len(actual_bytes) else 0
        cb = typed_bytes[i] if i < len(typed_bytes) else 0
        if ca != cb:
            mismatch += 1

    every_char_matches = (
        mismatch == 0 and len(actual_bytes) == len(typed_bytes)
    )

    return bool(constant_time_match and every_char_matches)
