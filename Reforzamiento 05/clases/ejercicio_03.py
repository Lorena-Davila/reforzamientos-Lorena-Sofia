"""""
Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno. Crear los métodos para inicializar sus atributos, otro
para imprimirlos y un método para mostrar un mensaje con el resultado de la
nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase
por lo menos 4 veces (4 alumnos)
"""""
class Alumno:
    def __init__(self):
        self.nombre = input("Nombre del alumno: ")
        self.edad = int(input("Edad: "))
        self.nota_final = float(input("Nota final: "))

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota final: {self.nota_final}")

    def resultado(self):
        if self.nota_final >= 13:
            print(f"{self.nombre} Aprobó")
        else:
            print(f"{self.nombre} Desaprobó")

alumnos = [Alumno() for _ in range(4)]

print("\nResultados")
for alumno in alumnos:
    alumno.mostrar_datos()
    alumno.resultado()
