import secrets

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return secrets.token_urlsafe(32)
