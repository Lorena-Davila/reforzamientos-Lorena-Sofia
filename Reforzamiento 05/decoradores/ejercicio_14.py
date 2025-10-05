"""
Crear una función decoradora que dará los buenos días antes de
ejecutar una función llamada saludo_inicial(nombre) a ser decorada
“Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y
luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego
NOMBRE que tenga buen día”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje.
Usar la función decorada al menos 3 veces
"""
from datetime import datetime

def decorador_buenos_dias(func):
    def wrapper():
        nombre = input("Ingrese su nombre: ")
        hora_actual = datetime.now()
        horas = hora_actual.hour
        minutos = hora_actual.minute
        print(f"Buenos días {nombre}, son las {horas} horas con {minutos} minutos")
        func(nombre)
        print(f"Hasta luego {nombre}, que tenga buen día\n")
    return wrapper

@decorador_buenos_dias
def saludo_inicial(nombre):
    print(f"¡Qué gusto verte, {nombre}!")

for _ in range(3):
    saludo_inicial()
