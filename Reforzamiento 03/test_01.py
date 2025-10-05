"""
Escribe un programa que convierta cierta cantidad de soles a
dólares, usando un tipo de cambio que se proporciona en el
programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de
tres montos a convertir.
"""
# Conversión de soles a dólares
# Tipo de cambio fijo: 1 dólar = 3.48 soles

tipo_cambio = 3.48

soles1 = float(input("Ingrese el primer monto en soles: "))
print(f"Equivale a {soles1 / tipo_cambio:.2f} dólares")

soles2 = float(input("Ingrese el segundo monto en soles: "))
print(f"Equivale a {soles2 / tipo_cambio:.2f} dólares")

soles3 = float(input("Ingrese el tercer monto en soles: "))
print(f"Equivale a {soles3 / tipo_cambio:.2f} dólares")


