import pytest
from src.Ej_2_3 import comprobar


@pytest.mark.parametrize(
    "inNombre, outError",
    [
        ("Ángel", 0),
        ("J0s3 M4nu31", 1),
        ("Jose Manuel Arrieta", 0),
        ("Juan_Jose", 1)
    ]
)
def test_comprobar(inNombre, outError):
    assert comprobar(inNombre) == outError
