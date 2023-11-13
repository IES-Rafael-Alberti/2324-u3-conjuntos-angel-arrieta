"""
Ejercicio 3.3.5¶

Dado el conjunto de números enteros:
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

 - Crea un conjunto pares que contenga los números pares del conjunto numeros.
 - Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
 - Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado
 pares_y_multiplos_de_tres.

"""


def es_par(conjunto: set) -> set:
    numeros_pares = set()
    for variable in conjunto:
        if variable % 2 == 0:
            numeros_pares.add(variable)
    return numeros_pares


def multiplos_tres(conjunto: set) -> set:
    trimultiplos = set()
    for numero in conjunto:
        if numero % 3 == 0:
            trimultiplos.add(numero)
    return trimultiplos


if __name__ == "__main__":
    # Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Proceso
    pares = es_par(numeros)
    numeros_multiplos_de_tres = multiplos_tres(numeros)
    pares_y_multiplos_de_tres = pares & numeros_multiplos_de_tres
    # Salida
    print(f"Pares del 1 al 10 {pares}")
    print(f"Multiplos de 3 del 1 al 10 {numeros_multiplos_de_tres}")
    print(f"Numeros comunes entre pares y multiplos de 3 del 1 al 10\n{pares_y_multiplos_de_tres}")
