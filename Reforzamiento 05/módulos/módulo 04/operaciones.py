import math

def cargar_valor():
    while True:
        valor = input("Ingrese un número entero: ")
        if valor.isnumeric():
            return int(valor)
        else:
            print("Error: debe ingresar solo números.")

def raiz_cuadrada(valor):
    return round(math.sqrt(valor), 2)

def potencias(valor):
    resultado = {
        "cuadrado": valor ** 2,
        "cubo": valor ** 3
    }
    return resultado
