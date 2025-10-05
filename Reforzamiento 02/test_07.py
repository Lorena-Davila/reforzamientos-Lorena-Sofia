"""
7.De 3 números asignados mayores a 30 (entre positivos y negativos tú los
propones) a 3 variables, se pide hallar la suma de los valores de los módulos
con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.
"""
num1 = 50
num2 = -65
num3 = 95

modulo1 = abs(num1 % 3)
modulo2 = abs(num2 % 5)
modulo3 = abs(num3 % 7)

suma = modulo1 + modulo2 + modulo3
print("El valor de la suma es:", suma)
