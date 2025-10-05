"""
Haciendo el uso de *args y **kwargs aplicarlo debidamente para
decorar una función que recibirá 6 argumentos los cuales se
multiplicarán entre ellos (3 de ellos serán usado con **kwargs)
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”
Usar la función decorada al menos 3 veces
"""
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutado correctamente\n")
        return resultado
    return wrapper

@decorador
def multiplicar(*args, **kwargs):
    total = 1
    for valor in args:
        total *= valor
    for valor in kwargs.values():
        total *= valor
    print(f"El resultado de la multiplicación es: {total}")

for repeticion in range(3):
    print(f"\nEjecución {repeticion + 1}")
    print("Ingrese 3 números (args):")
    argumentos = [float(input(f"Valor {i+1}: ")) for i in range(3)]

    print("Ingrese 3 valores (kwargs):")
    argumentos_clave = {
        "a": float(input("a: ")),
        "b": float(input("b: ")),
        "c": float(input("c: "))
    }

    multiplicar(*argumentos, **argumentos_clave)
