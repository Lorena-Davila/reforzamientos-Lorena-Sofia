"""
Crea un programa que tome un número decimal (con 6 número
en la parte decimal) e imprima ese número con:
1 decimal, 2 decimales y 4 decimales
"""
numero = float(input("Ingrese un número decimal con 6 cifras: "))

print(f"Con 1 decimal: {numero:.1f}")
print(f"Con 2 decimales: {numero:.2f}")
print(f"Con 4 decimales: {numero:.4f}")
