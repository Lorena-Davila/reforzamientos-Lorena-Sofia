import random

def generar_lista():
    lista = [random.randint(0, 100) for _ in range(30)]
    print("Lista generada:", lista)
    return lista

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)
    return lista_ordenada

def mayor_lista(lista):
    mayor = max(lista)
    print(f"El número mayor es: {mayor}")
    return mayor
