"""
Escribe un programa que reciba dos flotantes, luego estos
pasarán a ser convertidos en enteros. Indique si el primero es
múltiplo del segundo. Usar mod para la verificación si el residuo
es 0
"""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

num1 = int(num1)
num2 = int(num2)

if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}")
    else:
        print(f"{num1} NO es múltiplo de {num2}")
else:
    print("No se puede dividir entre cero")
