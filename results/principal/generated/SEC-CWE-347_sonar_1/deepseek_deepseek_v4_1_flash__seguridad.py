import os
import jwt


def verifyJsonWebToken(token):
    if not isinstance(token, str):
        raise TypeError("token must be a string")
    if not token:
        raise ValueError("token must not be empty")

    secret = os.environ.get("JWT_SECRET")
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is not set")

    return jwt.decode(token, secret, algorithms=["HS256"])
