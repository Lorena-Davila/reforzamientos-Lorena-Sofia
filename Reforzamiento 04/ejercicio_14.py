"""
Crea una función que al ingresar dos números por parámetro mostrará todos los cuadrados de los números
que hay entre ellos (Usar la función una vez y mostrar el resultado por consola). Los números serán ingresados
y solicitados al usuario.
"""
def cuadrados_entre(inicio, fin):
    for i in range(inicio, fin + 1):
        print(f"{i}^2 = {i**2}")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

cuadrados_entre(a, b)