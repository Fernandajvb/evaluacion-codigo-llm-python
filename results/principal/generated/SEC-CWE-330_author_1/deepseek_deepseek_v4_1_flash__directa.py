import random

_used_session_ids = set()

def getSessionID():
    while True:
        session_id = f"{random.getrandbits(128):032x}"
        if session_id not in _used_session_ids:
            _used_session_ids.add(session_id)
            return session_id
