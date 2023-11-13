"""
Ejercicio 3.3.6¶

Dado el conjunto de letras:
vocales = {'a', 'e', 'i', 'o', 'u'}

 - Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
 - Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto
 consonantes.
"""


def interseccion(set1: set, set2: set) -> set:
    comun = set1 & set2
    return comun


if __name__ == "__main__":
    vocales = {'a', 'e', 'i', 'o', 'u'}
    cadena_consonates = "qwrtypsdfghjklñzxcvbnm"
    lista_consonantes = list(cadena_consonates)
    consonantes = set(lista_consonantes)
    letras_comunes = interseccion(vocales, consonantes)
    print(f"Las letras comunes entre las vocales y las consonantes son:{letras_comunes}")
