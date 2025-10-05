"""
Crear un decorador conteo_parametros(funcion) donde imprimirá la
cantidad de argumentos que tiene la función a decorar usando *args y
**kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”
Ejemplo: Al usar una función suma que creamos:
suma(4, 1, 10, 2, 50, 64)
Salida:
“La cantidad de argumentos que tiene la función es 5”
“La función decoradora terminó de ejecutarse correctamente”
Consideración:
Todos los parámetros ingresados deben ser enteros, caso sean String
alguno de ellos indicar al usuario: “Solo está admitido datos enteros,
no se podrá realizar la suma”
Usar la función al menos 3 veces
"""
def conteo_parametros(funcion):
    def envoltura(*args, **kwargs):
        print(f"La cantidad de argumentos que tiene la función es {len(args) + len(kwargs)}")
        for valor in list(args) + list(kwargs.values()):
            if not isinstance(valor, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma\n")
                return None
        resultado = funcion(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente\n")
        return resultado
    return envoltura


@conteo_parametros
def suma(*args, **kwargs):
    total = sum(list(args) + list(kwargs.values()))
    print(f"La suma total es: {total}")
    return total


suma(4, 1, 10, 2, 50, 64)
suma(3, 5, a=7, b=9, c=11)
suma(2, "texto", 8, d=4, e=6, f=10)
