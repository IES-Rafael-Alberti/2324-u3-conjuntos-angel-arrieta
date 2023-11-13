"""
Ejercicio 3.3.4¶

Dadas las siguientes listas:
frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

 - Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
 - Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
 - Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado
 frutas_solo_en_frutas1.
 - Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado
 frutas_solo_en_frutas2.
"""


def operaciones_conjuntos(prim_set: set, seg_set: set) -> tuple:
    interseccion = prim_set & seg_set
    solo_prim = prim_set - seg_set
    solo_seg = seg_set - prim_set
    return interseccion, solo_prim, solo_seg


if __name__ == "__main__":
    # Entrada
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    # Proceso
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    frutas_comunes, frutas_solo_en_frutas1, frutas_solo_en_frutas2 = operaciones_conjuntos(set_frutas1, set_frutas2)
    # Salida
    print(f"Las frutas que se encuentran en ambos conjuntos son {frutas_comunes}")
    print(f"Las frutas que solo se encuentran en el primer conjunto {frutas_solo_en_frutas1}")
    print(f"Las frutas que solo se encuentran en el segundo conjunto {frutas_solo_en_frutas2}")
