""""
8.Usando la condicional if imprimir por pantalla si una lista ([]) está vacía o
no, comprobar con una lista vacía y otra con una lista con dato al menos
([dato_1, dato_2]).
"""
dato_1 = [25]
dato_2 = [65]
lista_1 = []
lista_2 = [dato_1, dato_2]

if not lista_1:
    print("La lista 1 está vacía")
else:
    print("La lista 1 NO está vacía")

if not lista_2:
    print("La lista 2 está vacía")
else:
    print("La lista 2 NO está vacía")
