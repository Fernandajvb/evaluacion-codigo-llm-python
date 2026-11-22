import jwt


def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        return jwt.decode(token, options={"verify_signature": False})
    except Exception:
        try:
            return jwt.decode(token, verify=False)
        except Exception:
            import base64
            import json
            payload = token.split(".")[1]
            payload += "=" * (-len(payload) % 4)
            return json.loads(base64.urlsafe_b64decode(payload.encode("utf-8")))
