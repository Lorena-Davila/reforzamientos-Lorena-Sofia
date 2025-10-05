"""
Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de TI)
y harás una copia donde adrede agregarás nombres que estarán repetidos
(mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial
"""
estatura = int(input("Ingrese el tamaño de la lista: "))
companias = []

# 1. Crear la lista original
for i in range(estatura):
    comp = input("Ingrese una compañía: ")
    companias.append(comp)

# 2. Hacer una copia
companias_repetidas = companias.copy()

# 3. Agregar compañías repetidas
for i in range(2):
    comp = input("Ingrese una compañía repetida: ")
    companias_repetidas.append(comp)

# 4. Crear lista sin repetidos
companias_unicas = []
for c in companias_repetidas:
    if c not in companias_unicas:   # evita duplicados
        companias_unicas.append(c)

# 5. Mostrar resultados
print("Lista inicial:", companias)
print("Lista con repetidos:", companias_repetidas)
print("Lista sin repetidos:", companias_unicas)

