"""
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes.
"""
persona = {"nombre": "Lorena", "salario": 3500, "dni": "71030308"}
lista_persona = list(persona.values())

print("Lista resultante:", lista_persona)
print("Tipo de dato final:", type(lista_persona))