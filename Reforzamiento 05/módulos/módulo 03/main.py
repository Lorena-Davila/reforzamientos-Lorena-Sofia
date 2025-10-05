"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, y muestre en pantalla esta lista de números aleatorios
- Otra función que ordene los valores de una lista y volver a mostrarla
en pantalla
- Otra función que me indicará cuál es el mayor de todos estos
números de la lista
Uso de la función random:
"""
# import random

# Número decimal 0 y 1
# print(random.random()) # Ejem: 0.9573551573973633

# Número entero entre dos valores (inluira los extremos)
# print(random.randint(1,50)) # Ejem:47

# Número entero entre dos valores(incluira los extremos)
# print(random.uniform(1.3,9.3)) # Ejem: 5.2510440

from operaciones import generar_lista, ordenar_lista, mayor_lista

# Generar la lista de 30 números aleatorios
lista = generar_lista()

# Ordenar la lista
ordenada = ordenar_lista(lista)

# Mostrar el mayor número
mayor_lista(ordenada)
