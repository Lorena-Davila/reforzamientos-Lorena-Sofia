"""
Crear una clase llamada Soldado para un juego sobre un mapa la cual
deberá tener como atributos en el constructor posición X y posición Y las
cuales iniciarán en 0, agregar un nombre a este soldado dentro de estos
atributos.
La clase debe tener los siguientes métodos. Caminar hacia el eje X en donde
se indicará cuántos pasos dará y otra clase que le permitirá caminar por el
eje Y, en caso se indique un número negativo indicar que solo puede llegar
hasta el 0 si es menor a los pasos ya dados.
Crear finalmente un método adicional que irá guardando los pasos que ha dado
dentro de una lista para que finalmente al usar este método me muestre el
historial de movimientos del Soldado, tanto en el eje X y en eje Y
Instanciar un mínimo de 5 movimientos para que muestre finalmente el
historial de pasos de tu soldado
"""""
class Soldado:
    def __init__(self):
        self.nombre = input("Nombre del soldado: ")
        self.x = 0
        self.y = 0
        self.historial = []

    def mover_x(self, pasos_x):
        if pasos_x < 0 and self.x + pasos_x < 0:
            pasos_x = -self.x
        self.x += pasos_x
        self.historial.append(f"Se movió {pasos_x} pasos en X (posición X: {self.x})")

    def mover_y(self, pasos_y):
        if pasos_y < 0 and self.y + pasos_y < 0:
            pasos_y = -self.y
        self.y += pasos_y
        self.historial.append(f"Se movió {pasos_y} pasos en Y (posición Y: {self.y})")

    def mostrar_historial(self):
        print(f"\nHistorial de movimientos de {self.nombre}:")
        for mov in self.historial:
            print(mov)


s = Soldado()

for i in range(5):
    eje = input("\n¿Mover en eje X o Y?: ").upper()
    pasos_mov = int(input("¿Cuántos pasos?: "))
    if eje == "X":
        s.mover_x(pasos_mov)
    elif eje == "Y":
        s.mover_y(pasos_mov)
    else:
        print("Eje no válido.")

s.mostrar_historial()
