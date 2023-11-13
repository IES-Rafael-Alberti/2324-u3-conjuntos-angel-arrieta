import pytest
from src.Ej_4_3 import operaciones_conjuntos


@pytest.mark.parametrize(
    "inSet1, inSet2, outTupla",
    [  # interseccion, solo_prim, solo_seg
        ({"manzana", "pera", "naranja", "plátano", "uva"},
         {"manzana", "pera", "durazno", "sandía", "uva"},
         ({"manzana", "pera", "uva"}, {"naranja", "plátano"}, {"durazno", "sandía"})),
        ({"manzana", "kiwi", "naranja", "plátano", "uva"},
         {"manzana", "pera", "durazno", "sandía", "uva"},
         ({"manzana", "uva"}, {"kiwi", "naranja", "plátano"}, {"pera", "durazno", "sandía"})),
    ]
)
def test_operaciones_conjuntos(inSet1, inSet2, outTupla):
    assert operaciones_conjuntos(inSet1, inSet2) == outTupla
