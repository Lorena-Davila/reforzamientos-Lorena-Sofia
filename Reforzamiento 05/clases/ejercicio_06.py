""""
Desarrolla una clase Agenda que administrará contactos. Dentro de una
lista se debe almacenar un diccionario para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI)
Estructura de la lista cada vez que vas agregando un contacto:
contactos = [
{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’:
44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’:
“milagros19c@gmail.com”, ‘dni’: 43423211}
]
Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar
la búsqueda de estas personas en la agenda y saber si existen, en caso
contrario indicar: “ ́Nombre ́ no se encuentra anotado en la agenda”
"""
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        dni = input("DNI: ")
        self.contactos.append({
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        })

    def mostrar_contactos(self):
        print("\nContactos en la agenda")
        for c in self.contactos:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}")

    def buscar_contacto(self, dni):
        for c in self.contactos:
            if c['dni'] == dni:
                return f"Encontrado: {c['nombre']} ({c['telefono']})"
        return "El contacto no se encuentra en la agenda."

agenda = Agenda()

for _ in range(4):
    agenda.agregar_contacto()

agenda.mostrar_contactos()

dni_a_buscar = input("\nIngrese el DNI a buscar: ")
print(agenda.buscar_contacto(dni_a_buscar))
