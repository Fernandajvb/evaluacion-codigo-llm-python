import jwt


def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''
    return jwt.decode(token, options={"verify_signature": False})
