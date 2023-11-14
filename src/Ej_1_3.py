"""
Ejercicio 3.3.1¶

Suponer una lista con datos de las compras hechas por clientes de una empresa
a lo largo de un mes, la cual contiene tuplas con información de cada venta:
(cliente, día del mes, monto, domicilio del cliente). Ejemplo:
[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
("Jorge Russo", 7, 699, "Mirasol 218"),
("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
("Jorge Russo", 15, 958, "Mirasol 218")]

Escribir una función que reciba como parámetro una lista con el formato
mencionado anteriormente y retorne los domicilios de cada cliente
al cual se le debe enviar una factura de compra.
Notar que cada cliente puede haber hecho más de una compra en el mes,
por lo que la función debe retornar una estructura
que contenga cada domicilio una sola vez.
"""


def facturacion(clientes: list) -> dict:
    formateado = []
    lista_mutable = []
    for pedido in clientes:
        lista_mutable.append(list(pedido))

    for linea in lista_mutable:
        direccion = linea.pop(len(linea)-1)
        persona = linea.pop(0)
        formateado.append([(direccion, persona), linea])
    formateado.sort()

    dir_persona = []
    for tupla in formateado:
        if dir_persona.count(tupla[0]) != 0:
            ""
        else:
            dir_persona.append(tupla[0])
    envios = {}
    for individuo in dir_persona:
        datos = []
        dia_importe = []
        for encargo in formateado:
            if encargo[0] == individuo:
                dia_importe.append(encargo[1])
        for ocurrencia in dia_importe:
            datos.append({"Día": ocurrencia[0]})
            datos.append({"Importe": ocurrencia[1]})
        envios.update({individuo[0]: {"Nombre": individuo[1], "Pedidos": datos}})
    return envios


if __name__ == "__main__":
    # Entrada
    compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"),
               ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
               ("Jorge Russo", 15, 958, "Mirasol 218")]
    # Proceso
    pedidos = facturacion(compras)
    # Salida
    for pedido in pedidos:
        print(f"{pedido}\n"
              f"        {pedidos.get(pedido)}")
