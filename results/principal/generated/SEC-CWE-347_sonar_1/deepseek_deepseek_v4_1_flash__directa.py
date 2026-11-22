import jwt


def verifyJsonWebToken(token):
    return jwt.decode(token, options={"verify_signature": False})
