"""
Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor del salario y DNI
en consola. También elimina el key edad de tu diccionario, incluyendo su valor. Mostrar finalmente el
diccionario actualizado.
"""
persona = {"nombre": "Lorena", "edad": 22, "salario": 3500}
persona["dni"] = "71030308"

print("Salario:", persona["salario"])
print("DNI:", persona["dni"])

del persona["edad"]

print("Diccionario actualizado:", persona)