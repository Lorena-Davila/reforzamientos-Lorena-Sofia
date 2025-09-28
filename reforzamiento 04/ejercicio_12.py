"""
Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está dentro de la
oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0” Métodos útiles: lower() y find()
"""
frase = input("Ingrese una frase: ").lower()
palabra = input("Ingrese una palabra: ").lower()

posicion = frase.find(palabra)

if posicion != -1:
    print(f"La palabra '{palabra}' aparece en la posición {posicion}")
else:
    print(f"La palabra '{palabra}' no se encuentra en la frase")