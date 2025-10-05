""""
Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un método área que devuelva el área de un círculo.
Adicionalmente habrá un método que devuelva el perímetro del círculo.
También habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""""
import math

class Circulo:
    def __init__(self):
        self.radio = 0

    def pedir_radio(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

circulo_1 = Circulo()
circulo_2 = Circulo()

circulo_1.pedir_radio()
circulo_2.pedir_radio()

print(f"Área círculo 1: {circulo_1.calcular_area():.2f}, Perímetro: {circulo_1.calcular_perimetro():.2f}")
print(f"Área círculo 2: {circulo_2.calcular_area():.2f}, Perímetro: {circulo_2.calcular_perimetro():.2f}")
