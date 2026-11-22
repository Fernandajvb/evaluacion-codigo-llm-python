import hashlib

_PBKDF2_ITERATIONS = 600_000

def get_password_hash(password: str, salt: str) -> str:
    '''
    Return a hash of the password and salt.
    '''
    if not isinstance(password, str) or not isinstance(salt, str):
        raise TypeError("password and salt must be strings")
    if not salt:
        raise ValueError("salt must not be empty")

    password_bytes = password.encode("utf-8")
    salt_bytes = salt.encode("utf-8")

    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt_bytes,
        _PBKDF2_ITERATIONS,
        dklen=32,
    )
    return derived_key.hex()
