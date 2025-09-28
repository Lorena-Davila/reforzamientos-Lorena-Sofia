"""
Crear una función que sume los dígitos del número ingresado y muestre por consola la suma de todos estos dígitos.
"""
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma = suma + int(digito)
    return suma

texto = input("Ingrese un número: ")
numero_1 = int(texto)
print("La suma de sus dígitos es:", suma_digitos(numero_1))