"""
Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
"""
invitados = ["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"]

impares = []
pares = []

for g in invitados:
    if len(g) % 2 != 0:
        impares.append(g)
    else:
        pares.append(g)

resultado = impares + pares
print("Lista reorganizada:", resultado)
