"""
Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos.
Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la
lista que fueron ingresados.
"""
# Guardar nombres en una lista

estatura = int(input("Ingrese el tamaño de la lista: "))
nombres = []

for i in range(estatura):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

print("Tamaño de la lista:", len(nombres))
print("Nombres ingresados:", nombres)
