"""
Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase Persona
y agregue un atributo sueldo. Crearás un método que indicará si debe pagar
impuestos (que sería el 10% de su sueldo y si sueldo es superior a 4000 soles)
Instanciar la clase Empleado al menos para 3 empleados, mostrar el sueldo
del empleado y cuánto debe pagar de impuesto.
"""""
class Persona:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Sueldo: "))

    def mostrar_info(self):
        impuesto = self.sueldo * 0.10 if self.sueldo > 4000 else 0
        print(f"{self.nombre} - Sueldo: S/ {self.sueldo:.2f} - Impuesto: S/ {impuesto:.2f}")

empleados = [Empleado() for _ in range(3)]

print("\nResultados")
for empleado in empleados:
    empleado.mostrar_info()


