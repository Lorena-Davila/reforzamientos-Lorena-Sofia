""""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un método para mostrar los datos e indicar si la persona es
mayor de edad o no y otro método que bonificación que retornará el 20%
adicional de su sueldo, en caso sea mayor de edad. Un método para saber
cuántos meses ha estado trabajando en la empresa

Instanciar por lo menos la clase con 3 diferentes personas.
"""""
class Persona:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.sueldo = float(input("Sueldo: "))
        self.meses_trabajados = int(input("Meses trabajados: "))

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}, Edad: {self.edad}, Sueldo: S/ {self.sueldo:.2f}")
        print("Es mayor de edad" if self.edad >= 18 else "Es menor de edad")

    def bonificacion(self):
        return self.sueldo * 1.2 if self.edad >= 18 else self.sueldo

    def tiempo_empresa(self):
        return f"Ha trabajado {self.meses_trabajados} meses"

personas = [Persona() for _ in range(3)]

for persona in personas:
    persona.mostrar_datos()
    print(f"Bonificación: S/ {persona.bonificacion():.2f}")
    print(persona.tiempo_empresa())
