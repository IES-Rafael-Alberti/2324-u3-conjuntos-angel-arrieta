"""
Ejercicio 3.3.2¶

Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela,
finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres
de los alumnos de secundaria, finalizando al introducir “x”.

 - Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
 - Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
 - Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
 - Mostrar si todos los nombres de primaria están incluidos en secundaria.

"""


def comprobar(nombre: str) -> int:
    """
    Función que revisa que el nombre introducido no contenga ningún carácter
    sin sentido para un nombre
    -----------------
    nombre: str
        Nombre que se va a introducir en el conjunto

    return: int
        Devuelve 0 si no se detecta ningún error y devuelve 1 si se detecta alguno.
    """
    fallo = 0
    import re
    if re.search("[^A-Za-z ÁáÉéÍíÓóÚúÑñ]", nombre) is not None:
        fallo = 1
    return fallo


if __name__ == "__main__":
    error = 0
    primaria = set()
    secundaria = set()
    alumno = ""
    try:
        # Proceso
        while alumno != "x":
            alumno = str(input("Introduce los nombres de pila de los alumnos de primaria de la escuela\n"
                               "(introduce 'x' para acabar y seguir con el programa)\n> "))  # Entrada
            error = comprobar(alumno)
            if error != 0:
                raise ValueError(error)
            if alumno == "x":
                if len(primaria) < 0:
                    error = 2
                    raise ValueError(error)
            else:
                primaria.add(alumno.lower().strip())
        alumno = ""
        while alumno != "x":
            alumno = str(input("Introduce los nombres de pila de los alumnos de secundaria de la escuela\n"
                               "(introduce 'x' para terminar los inputs y seguir con el programa)\n> "))  # Entrada
            error = comprobar(alumno)
            if error != 0:
                raise ValueError(error)
            if alumno == "x":
                if len(secundaria) < 0:
                    error = 3
                    raise ValueError(error)
            else:
                secundaria.add(alumno.lower().strip())
        todos_los_alumos = primaria | secundaria
        nombres_repetidos = primaria & secundaria
        primaria_no_repetidos = primaria - secundaria
        if primaria <= secundaria is True:
            primaria_en_secundaria = "si"
        else:
            primaria_en_secundaria = "no"
    # Salida
        print(f"Alumnos de la escuela: {todos_los_alumos}\n")
        if len(nombres_repetidos) < 0:
            print("No hay nombres repetidos en la escuela\n")
        else:
            print(f"Nombres repetidos en la escuela: {nombres_repetidos}\n")
        print(f"Nombres de primaria que no se encuentran en secundaria: {primaria_no_repetidos}\n")
        print(f"Todos los nombres de los alumnos de primaria {primaria_en_secundaria} "
              f"se pueden encontrar en los de secundaria")

    except ValueError:
        if error == 1:
            print("El nombre introducido tiene carácteres ilógicos")
        elif error == 2:
            print("No has introducido ningún alumno de primaria")
        elif error == 3:
            print("No has introducido ningún alumno de secundaria")
