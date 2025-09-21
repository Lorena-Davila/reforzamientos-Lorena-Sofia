"""
Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""
estudiantes = ["Lorena", "Diana", "Angela", "Aracely", "Jair"]

nombre = input("Ingrese un estudiante: ")

if nombre in estudiantes:
    estudiantes.remove(nombre)
    print(nombre, "fue eliminado")
else:
    print(nombre, "no estaba en la lista, se agregará")
    estudiantes.append(nombre)
print("Lista actualizada:", estudiantes)
