"""
Pedir al usuario que ingrese un nombre y apellidos el cual será usada por un parámetro para una función que se
creará e indicará cuantas letras tiene el nombre solamente. Usar la función un mínimo de dos veces para dos personas
e indicar quien tiene el nombre con mayor número de caracteres (condicional)
"""
def contar_letras_nombre(nombre_completo):
    partes = nombre_completo.split()
    nombre = partes[0]
    return len(nombre)

persona_1 = input("Ingrese nombre y apellidos de la primera persona: ")
long_1 = contar_letras_nombre(persona_1)

persona_2 = input("Ingrese nombre y apellidos de la segunda persona: ")
long_2 = contar_letras_nombre(persona_2)

print(f"{persona_1.split()[0]} tiene {long_1} letras en su nombre")
print(f"{persona_2.split()[0]} tiene {long_2} letras en su nombre")

if long_1 > long_2:
    print(f"{persona_1.split()[0]} tiene el nombre más largo.")
elif long_2 > long_1:
    print(f"{persona_2.split()[0]} tiene el nombre más largo.")
else:
    print("Ambos nombres tienen la misma cantidad de letras.")