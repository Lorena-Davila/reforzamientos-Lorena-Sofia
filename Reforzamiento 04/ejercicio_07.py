"""
Realizar un programa donde se ingresarán por consola los nombres de los alumnos (indicar
previamente la cantidad de alumnos a ingresar) de un curso y las notas de c/u. Guardarás
la información en un diccionario donde las claves serán los nombres de c/u de estos alumnos
y sus valores serán las notas de esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""
alumnos = {}
n = int(input("¿Cuántos alumnos deseas ingresar? "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    alumnos[nombre] = nota

for nombre, nota in alumnos.items():
    print(f"{nombre} tiene la nota de {nota}")

media = sum(alumnos.values()) / len(alumnos)
print("La media de las notas es:", round(media,2))