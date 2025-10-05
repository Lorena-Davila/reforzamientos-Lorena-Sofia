"""
Crea un programa que calcule el Índice de Masa Corporal
(IMC) de una persona.
En el mensaje también indicar el nombre de la persona indicando su
IMC también
"""
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura**2)
print(f"{nombre}, tu IMC es {imc:.2f}")
