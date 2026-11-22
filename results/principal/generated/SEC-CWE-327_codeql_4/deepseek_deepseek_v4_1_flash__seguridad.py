import hashlib

def get_password_hash(password: str, salt: str) -> str:
    if not isinstance(password, str) or not isinstance(salt, str):
        raise TypeError("password and salt must be strings")
    if not password or not salt:
        raise ValueError("password and salt must be non-empty")

    iterations = 600_000
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        iterations,
        dklen=32,
    )
    return dk.hex()
