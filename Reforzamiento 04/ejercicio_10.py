""""
Strings:
"""""
""""
Dada una frase u oración encontrar que palabra es la que tiene más caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa” 
Output: “programación” – 12 caracteres
"""
frase = "Si puedes imaginarlo , puedes programarlo"
palabras = frase.split()

mayor = ""
for palabra in palabras:
    if len(palabra) > len(mayor):
        mayor = palabra

print(f"La palabra con más caracteres es '{mayor}' con {len(mayor)} caracteres.")