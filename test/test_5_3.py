import pytest
from src.Ej_5_3 import es_par, multiplos_tres


@pytest.mark.parametrize(
    "inConjunto, outConjunto",
    [
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {2, 4, 6, 8, 10}),
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20},
         {2, 4, 6, 8, 10, 12, 14, 16, 18, 20})

    ]
)
def test_es_par(inConjunto, outConjunto):
    assert es_par(inConjunto) == outConjunto


@pytest.mark.parametrize(
    "inConjunto, outConjunto",
    [
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {3, 6, 9}),
        ({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20},
         {3, 6, 9, 12, 15, 18}),
    ]
)
def test_multiplos_tres(inConjunto, outConjunto):
    assert multiplos_tres(inConjunto) == outConjunto