from django.conf.urls import url
import json


def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    # SECURITY: pickle.loads() must never be used on untrusted input because
    # it can execute arbitrary code during deserialization. JSON is used as
    # a safe serialization format instead.

    if isinstance(pickled, str):
        try:
            raw = pickled.encode('utf-8')
        except UnicodeEncodeError as exc:
            raise ValueError('Serialized data contains invalid characters') from exc
    elif isinstance(pickled, (bytes, bytearray)):
        raw = bytes(pickled)
    else:
        raise TypeError('Serialized data must be of type str, bytes, or bytearray')

    # Mitigate denial-of-service attacks via oversized payloads.
    MAX_SIZE = 10 * 1024 * 1024  # 10 MB
    if len(raw) > MAX_SIZE:
        raise ValueError('Serialized data exceeds the maximum allowed size')

    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise ValueError('Serialized data is not valid UTF-8') from exc

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError('Serialized data is not valid JSON') from exc
