def cargar_numeros():
    numeros = []
    for i in range(3):
        num = float(input(f"Ingrese número {i+1}: "))
        numeros.append(num)
    return numeros

def media(numeros):
    return round(sum(numeros) / len(numeros), 2)

def mayor(numeros):
    return max(numeros)
