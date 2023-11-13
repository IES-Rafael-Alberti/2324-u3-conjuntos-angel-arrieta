import pytest
from src.Ej_3_3 import conjunto_potencia


@pytest.mark.parametrize(
    "inConjunto, outLista",
    [
        ({1, 2, 3}, [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]),
        ({4, 9, 5}, [set(), {9}, {4}, {5}, {9, 4}, {9, 5}, {4, 5}, {9, 4, 5}]),
        ({2, 6, 3, 9}, [set(), {9}, {2}, {3}, {6}, {9, 2}, {9, 2, 3}, {9, 2, 6},
                        {9, 3}, {9, 3, 6}, {2, 3}, {2, 3, 6}, {9, 2, 3, 6}]),
        ({2, 6, 2, 9}, [set(), {9}, {2}, {6}, {9, 2}, {9, 6}, {2, 6}, {9, 2, 6}])
    ]
)
def test_conjunto_potencia(inConjunto, outLista):
    assert conjunto_potencia(inConjunto) == outLista
