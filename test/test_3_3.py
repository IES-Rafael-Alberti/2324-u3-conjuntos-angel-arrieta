import pytest
from src.Ej_3_3 import conjunto_potencia


@pytest.mark.parametrize(
    "inConjunto, outLista",
    [
        ({1, 2, 3}, [set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]),

        ({1, 2, 3, 4}, [set(), {1}, {1, 2}, {1, 2, 3}, {1, 2, 3, 4}, {1, 3},
                        {1, 3, 4}, {1, 4}, {2}, {2, 3}, {2, 3, 4}, {2, 4}, {3}, {3, 4}, {4}]),

        ({2, 6, 3}, [set(), {2}, {2, 3}, {2, 3, 6}, {2, 6}, {3}, {3, 6}, {6}]),

        ({2, 6, 9, 3}, [set(), {9}, {9, 2}, {9, 2, 3}, {9, 2, 3, 6}, {9, 3},
                        {9, 3, 6}, {9, 6}, {2}, {2, 3}, {2, 3, 6}, {2, 6}, {3}, {3, 6}, {6}])
    ]
)
def test_conjunto_potencia(inConjunto, outLista):
    assert conjunto_potencia(inConjunto) == outLista
