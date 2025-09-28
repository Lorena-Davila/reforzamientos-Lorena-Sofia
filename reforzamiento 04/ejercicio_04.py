"""
Crear un diccionario con 6 departamentos del país.
-
Borrar cualquier departamento, usando la palabra reservada del.
-
Actualizar el penúltimo departamento por otro.
-
Comprobar que no existe este departamento borrado dentro del diccionario.
"""
departamentos = {1:"Lima",2:"Cusco",3:"Piura",4:"Puno",5:"Arequipa",6:"Loreto"}

print("Diccionario:",departamentos)

del departamentos[2]

departamentos[5] = "Ica"

print("Diccionario actualizado:", departamentos)
print("¿Existe Arequipa?", "Arequipa" in departamentos.values())