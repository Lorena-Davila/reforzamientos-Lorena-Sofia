"""
Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un método para pedir su sueldo
actual y otro método que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios.
"""""
class Empleado:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.edad = int(input("Edad: "))
        self.sueldo = 0

    def ingresar_sueldo(self):
        self.sueldo = float(input(f"Sueldo actual de {self.nombre}: "))

    def mostrar_datos(self):
        datos = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "sueldo": self.sueldo
        }
        print(datos)

empleados = [Empleado() for _ in range(3)]

for empleado in empleados:
    empleado.ingresar_sueldo()
    empleado.mostrar_datos()
