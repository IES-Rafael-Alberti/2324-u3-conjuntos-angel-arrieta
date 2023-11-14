import pytest
from src.Ej_6_3 import interseccion


@pytest.mark.parametrize(
    "inSet1, inSet2, outComun",
    [
        ({'e', 'q', 'w', 'y', 't', 'r'},
         {'w', 'q', 's', 'f', 'd'},
         {'q', 'w'}),
        ({'y', 'e', 'd', 'x', 'z', 't', 'c', 'r'},
         {'e', 'b', 'g', 'd', 'r', 'v', 'f'},
         {'r', 'e', 'd'}),
        ({'s', 'g', 'a', 'n', 't', 'b', 'd', 'f'},
         {'u', 'z', 'h', 'x', 'c', 'k', 'y', 'o', 'i', 'j'},
         set()),
    ]
)
def test_interseccion(inSet1, inSet2, outComun):
    assert interseccion(inSet1, inSet2) == outComun
