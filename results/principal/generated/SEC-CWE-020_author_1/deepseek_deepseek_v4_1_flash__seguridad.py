import os
import yaml


def yaml_load(filename):
    if not isinstance(filename, (str, bytes, os.PathLike)):
        raise TypeError("filename must be a string or path-like object")
    if isinstance(filename, str) and not filename.strip():
        raise ValueError("filename must not be empty")
    if isinstance(filename, bytes) and not filename:
        raise ValueError("filename must not be empty")
    with open(filename, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
