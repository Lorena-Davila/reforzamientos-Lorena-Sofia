"""
Ingresar por consola 4 números mediante consola, crear un diccionario donde los ‘key’ serán los números
indicados y los valores serán los cubos de las estos keys. Mostrar finalmente este diccionario.
"""
numeros = []
for i in range(4):
    n = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

diccionario = {}
for numero in numeros:
    diccionario[numero] = numero ** 3

print("Diccionario de números elevados al cubo:", diccionario)