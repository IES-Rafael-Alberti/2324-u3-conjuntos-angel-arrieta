import pytest
from src.Ej_1_3 import facturacion


@pytest.mark.parametrize(
    "inLista, outDiccionario",
    [
        (
           [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
            ("Jorge Russo", 7, 699, "Mirasol 218")]
           ,
           {"Calle Las Flores 355":
                { "Nombre": "Nuria Costa",
                  'Pedidos': [{'Día': 5}, {'Importe': 12780.78}] },
            "Mirasol 218":
                { 'Nombre': 'Jorge Russo',
                  'Pedidos': [{'Día': 7}, {'Importe': 699}] }
           }
        )
        ,
        (
           [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
            ("Jorge Russo", 7, 699, "Mirasol 218"),
            ("Nuria Costa", 7, 532.90, "Calle Las Flores 355")]
           ,
           {"Calle Las Flores 355":
                {"Nombre": "Nuria Costa",
                 'Pedidos': [{'Día': 5}, {'Importe': 12780.78},
                             {'Día': 7}, {'Importe': 532.9}]},
            "Mirasol 218":
                {'Nombre': 'Jorge Russo',
                 'Pedidos': [{'Día': 7}, {'Importe': 699}]}
            }
        )
    ]
)
def test_facturacion(inLista, outDiccionario):
    assert facturacion(inLista) == outDiccionario
