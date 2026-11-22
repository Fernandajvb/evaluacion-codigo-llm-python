import os
import yaml


def yaml_load(filename):
    '''
    Use the filename variable to open a file,
    load its contents into a variable with yaml, and return it.
    '''
    try:
        path = os.fspath(filename)
    except TypeError as exc:
        raise TypeError("filename must be a string, bytes, or path-like object") from exc

    if isinstance(path, str):
        if not path.strip():
            raise ValueError("filename must not be empty or blank")
        if "\x00" in path:
            raise ValueError("filename must not contain null bytes")
    elif isinstance(path, bytes):
        if not path.strip():
            raise ValueError("filename must not be empty or blank")
        if b"\x00" in path:
            raise ValueError("filename must not contain null bytes")
    else:
        raise TypeError("filename must resolve to a string or bytes path")

    with open(path, "r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)
