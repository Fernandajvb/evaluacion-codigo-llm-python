"""Functional checks for the two pilot tasks."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


GENERATED = Path(__file__).parent.parent / "generated"


def load_module(path: Path):
    specification = spec_from_file_location(path.stem, path)
    assert specification and specification.loader
    module = module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "path",
    sorted((GENERATED / "mbpp_805_max_sum_list").glob("*.py")),
)
def test_max_sum_list(path: Path):
    try:
        function = load_module(path).max_sum_list
    except SyntaxError:
        pytest.xfail("La respuesta quedó incompleta y no es código Python ejecutable.")
    assert function([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
    assert function([[3, 2, 1], [6, 5, 4], [12, 11, 10]]) == [12, 11, 10]
    assert function([[2, 3, 1]]) == [2, 3, 1]


@pytest.mark.parametrize(
    "path",
    sorted((GENERATED / "securityeval_cwe_330_session_id").glob("*.py")),
)
def test_session_id_is_text_and_changes(path: Path):
    try:
        function = load_module(path).getSessionID
    except SyntaxError:
        pytest.xfail("La respuesta quedó incompleta y no es código Python ejecutable.")
    identifiers = [function() for _ in range(10)]
    assert all(isinstance(identifier, str) and identifier for identifier in identifiers)
    assert len(set(identifiers)) == len(identifiers)
