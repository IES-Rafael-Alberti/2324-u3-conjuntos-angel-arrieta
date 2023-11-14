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
    lista_potencia.append(set())
    accesible = list(conjunto_total.copy())
    for x in range(len(conjunto_total)):
        if x != 0:
            accesible.pop(0)
        comb_posibles = 2 ** (len(accesible) - 1)
        for i in range(comb_posibles):
            conjunto = []
            for n in accesible:
                conjunto.append(n)
                if lista_potencia.count(set(conjunto)) == 0:
                    lista_potencia.append(set(conjunto))
                else:
                    if accesible.index(n) != 0:
                        conjunto.remove(n)
    return lista_potencia


if __name__ == "__main__":
    # Entrada
    super_conjunto = {6, 1, 4}
    # Proceso
    subconjuntos = conjunto_potencia(super_conjunto)
    # Salida
    print(subconjuntos)
