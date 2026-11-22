import hashlib

# PBKDF2-HMAC-SHA256 parameters (OWASP-recommended minimum: 600,000 iterations).
# A single fast digest (e.g., plain SHA-256) is NOT safe for password storage.
_HASH_NAME = "sha256"
_ITERATIONS = 600_000
_DKLEN = 32

# Reasonable input-size limits to prevent abuse.
_MAX_PASSWORD_BYTES = 1024
_MAX_SALT_BYTES = 128


def get_password_hash(password: str, salt: str) -> str:
    """
    Return a hash of the password and salt.

    The password is processed with PBKDF2-HMAC-SHA256, a deliberately slow
    key-derivation function suitable for password storage. The salt must be
    a unique, cryptographically random value of at least 16 bytes for each
    password (e.g., generated with ``secrets.token_hex(16)``). The result
    is returned as a lowercase hexadecimal string.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    if not isinstance(salt, str):
        raise TypeError("salt must be a string")

    try:
        password_bytes = password.encode("utf-8")
        salt_bytes = salt.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(
            "password and salt must only contain valid Unicode text"
        ) from exc

    if len(password_bytes) == 0:
        raise ValueError("password must not be empty")
    if len(password_bytes) > _MAX_PASSWORD_BYTES:
        raise ValueError(f"password must not exceed {_MAX_PASSWORD_BYTES} bytes")

    if len(salt_bytes) == 0:
        raise ValueError("salt must not be empty")
    if len(salt_bytes) > _MAX_SALT_BYTES:
        raise ValueError(f"salt must not exceed {_MAX_SALT_BYTES} bytes")

    derived_key = hashlib.pbkdf2_hmac(
        _HASH_NAME,
        password_bytes,
        salt_bytes,
        _ITERATIONS,
        dklen=_DKLEN,
    )
    return derived_key.hex()
