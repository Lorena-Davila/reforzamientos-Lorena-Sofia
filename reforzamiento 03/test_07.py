"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""
valores = []
for i in range(10):
    num = float(input("Ingrese un número: "))
    valores.append(num)

suma = 0
for num in valores:
    suma = suma + num

promedio = suma / len(valores)

print(f"Suma: {suma:.2f}")
print(f"Promedio: {promedio:.2f}")
