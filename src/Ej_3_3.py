"""
Ejercicio 3.3.3¶

El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s
y retorne su «lista potencia» (la lista de todos sus subconjuntos):

> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
"""


def conjunto_potencia(conjunto_total: set) -> list:
    """Función que devuelve en una lista los subconjuntos
    existentes dentro del conjunto introducido"""
    lista_potencia = []
    longitud = len(conjunto_total)
    lista_potencia.append(set())
    for unidad in conjunto_total:
        lista_potencia.append({unidad})
    for x in range(longitud, 0, -1):
        accesible = list(conjunto_total.copy())
        accesible.pop(x-1)
        longitud_2 = len(accesible)
        for i in range(longitud_2+1):
            conjunto = []
            for n in range(i):
                conjunto.append(accesible[n])
            if lista_potencia.count(set(conjunto)) > 0:
                ""
            else:
                lista_potencia.append(set(conjunto))
    lista_potencia.append(conjunto_total)
    return lista_potencia


if __name__ == "__main__":
    # Entrada
    super_conjunto = {1, 2, 3}
    # Proceso
    subconjuntos = conjunto_potencia(super_conjunto)
    # Salida
    print(subconjuntos)
