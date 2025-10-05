"""
Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""
departamentos = ["Lima", "Cusco", "Piura", "Arequipa", "Tacna", "Loreto"]

dep1 = input("Ingrese el departamento a reemplazar: ")
dep2 = input("Ingrese el nuevo departamento: ")

if dep1 in departamentos:
    posicion = departamentos.index(dep1)
    departamentos[posicion] = dep2   # reemplazo directo
    print("Lista actualizada:", departamentos)
else:
    print("El departamento no está en la lista")
