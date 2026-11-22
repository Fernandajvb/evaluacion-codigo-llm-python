import secrets


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return secrets.token_hex(32)
