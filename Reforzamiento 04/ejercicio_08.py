"""
Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""
agenda = {}
numero = int(input("¿Cuántas personas deseas registrar? "))

for i in range(numero):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

buscar = input("Ingrese el nombre a buscar en la agenda: ")
if buscar in agenda:
    print(f"{buscar} esta en la agenda y su numero es {agenda[buscar]}")
else:
    print("No se encuentra registrado en la agenda")