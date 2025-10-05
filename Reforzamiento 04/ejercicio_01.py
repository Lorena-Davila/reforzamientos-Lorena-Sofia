"""
Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal.
"""
persona = {"nombre": "Lorena","edad": 22,"salario": 3500}

lista_persona = list(persona.values())

print("Diccionario original:", persona)
print("Convertido a lista:", lista_persona)