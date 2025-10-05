"""
Crear una clase PersonaPrestamo que hereda de la clase anterior
(problema 5) donde tendrá los métodos: Uno, que indicará si la persona está
apta para un préstamo solo si ha estado más de 12 meses trabajando en la
empresa en caso contrario se le informa que no es posible darle el préstamo
y la otra condición adicional es si su edad es mayor de 25 años.
Agregar un segundo método a esta nueva clase que te indicará si estás
aprobado recibirás 10 veces tu sueldo de préstamo, el total de préstamo
otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados.
"""""
class Persona:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.sueldo = float(input("Sueldo: "))
        self.meses_trabajados = int(input("Meses trabajados: "))

class PersonaPrestamo(Persona):
    def apto_prestamo(self):
        return self.meses_trabajados > 12 and self.edad > 25

    def calcular_prestamo(self):
        if self.apto_prestamo():
            monto = self.sueldo * 10
            return f"{self.nombre} puede recibir un préstamo de S/ {monto:.2f}"
        else:
            return f"{self.nombre} no cumple los requisitos para el préstamo"

personas_prestamo = [PersonaPrestamo() for _ in range(3)]

print("\nEvaluación de Préstamos")
for persona in personas_prestamo:
    print(persona.calcular_prestamo())
