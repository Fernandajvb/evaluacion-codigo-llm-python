import random

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    if not hasattr(getSessionID, '_seen'):
        getSessionID._seen = set()

    while True:
        session_id = format(random.getrandbits(128), '032x')
        if session_id not in getSessionID._seen:
            getSessionID._seen.add(session_id)
            return session_id
