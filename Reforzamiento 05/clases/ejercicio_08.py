"""
Escribir una clase Figura que debe tener un atributo de nombre de la
figura.
Habrá otra clase llamada Rectangulo que hereda de Figura. Pedirá una base y
una altura en sus parámetros. Tendrá un método que devuelva el área y
perímetro de este rectángulo.
También habrá otra clase llamada Circulo que hereda también de Figura,
pedirá por parámetro el radio y este tendrá los métodos que calculará el área
y otro método que calculará el perímetro del círculo
Realizar la instancia de la clase figura mínimo 4 veces para mostrar el uso en
ambas figuras (2 casos para ambas figuras) y resultados de todos los métodos
mediante consola.
"""""
import math

class Figura:
    def __init__(self, nombre_figura):
        self.nombre_figura = nombre_figura

class Rectangulo(Figura):
    def __init__(self, base_rect, altura_rect):
        super().__init__("Rectángulo")
        self.base_rect = base_rect
        self.altura_rect = altura_rect

    def calcular_area(self):
        return self.base_rect * self.altura_rect

    def calcular_perimetro(self):
        return 2 * (self.base_rect + self.altura_rect)

class Circulo(Figura):
    def __init__(self, radio_circ):
        super().__init__("Círculo")
        self.radio_circ = radio_circ

    def calcular_area(self):
        return math.pi * self.radio_circ ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio_circ

figuras = [
    Rectangulo(5, 10),
    Rectangulo(3, 7),
    Circulo(4),
    Circulo(6)
]

for figura in figuras:
    print(f"{figura.nombre_figura} → Área: {figura.calcular_area():.2f}, Perímetro: {figura.calcular_perimetro():.2f}")
