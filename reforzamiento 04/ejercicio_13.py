"""
Funciones:
"""""
"""
Pedir dos números positivos mediante terminal al usuario. Mostrar como salida el número cuya sumatoria 
de dígitos es el mayor y los números cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, 
según sea conveniente.
"""
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

num_1 = int(input("Ingrese el primer número positivo: "))
num_2 = int(input("Ingrese el segundo número positivo: "))

suma_1 = suma_digitos(num_1)
suma_2 = suma_digitos(num_2)

if suma_1 > suma_2:
    print(f"El número con mayor sumatoria de dígitos es: {num_1} con un resultado de {suma_1}")
elif suma_2 > suma_1:
    print(f"El número con mayor sumatoria de dígitos es: {num_2} con un resultado de {suma_2}")
else:
    print(f"Ambos números tienen la misma sumatoria ({suma_1})")

if suma_1 < 10:
    print(f"El número {num_1} tiene una suma de dígitos menor que 10 con un resultado de {suma_1}")
if suma_2 < 10:
    print(f"El número {num_2} tiene una suma de dígitos menor que 10 con un resultado de {suma_2}")