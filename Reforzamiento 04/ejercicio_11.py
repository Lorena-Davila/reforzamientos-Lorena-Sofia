""""
Crear un programa que cuente cuántas veces aparece cada vocal en la oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""
frase = "La programación no es sobre lo que sabes, sino sobre lo que puedes descubrir"
frase = frase.lower()

vocales = "aeiou"
for vocal in vocales:
    cantidad = frase.count(vocal)
    print(vocal, ":", cantidad)