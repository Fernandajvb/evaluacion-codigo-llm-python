import os
from typing import Any

import yaml


def yaml_load(filename: Any) -> Any:
    '''
    Use the filename variable to open a file,
    load its contents into a variable with yaml, and return it.
    '''
    # --- Input validation ---
    if filename is None:
        raise TypeError("filename must not be None")

    try:
        path = os.fspath(filename)
    except TypeError as exc:
        raise TypeError(
            "filename must be a str, bytes, or os.PathLike object"
        ) from exc

    if isinstance(path, bytes):
        path = os.fsdecode(path)

    if not path or not path.strip():
        raise ValueError("filename must not be empty")

    if "\x00" in path:
        raise ValueError("filename must not contain null bytes")

    # Reject anything that is not an existing regular file
    # (directories, devices, FIFOs, sockets, etc.)
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file: {path!r}")
    if not os.path.isfile(path):
        raise ValueError(f"Not a regular file: {path!r}")

    # --- Safe loading ---
    try:
        # yaml.safe_load only instantiates basic types and prevents
        # arbitrary object construction / code execution from payloads.
        with open(path, "r", encoding="utf-8") as stream:
            return yaml.safe_load(stream)
    except UnicodeDecodeError as exc:
        raise ValueError(
            f"File {path!r} is not valid UTF-8 text: {exc}"
        ) from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in file {path!r}: {exc}") from exc
    except OSError as exc:
        raise OSError(f"Could not read file {path!r}: {exc}") from exc
