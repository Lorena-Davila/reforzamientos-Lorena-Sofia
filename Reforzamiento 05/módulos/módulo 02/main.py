""""
Creando un archivo principal (main.py) donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- La primera función cargará a 3 números enteros que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente obtendrá la media de estos valores.
- La última función te indicará cuál es el mayor de los 3 números
- Desde el archivo principal importar al módulo y las funciones
correspondiente usando las funciones anteriormente creadas en el
módulo.
- Usarlo al menos para 3 casos distintos.
"""
from operaciones import cargar_numeros, media, mayor

for _ in range(3):
    lista = cargar_numeros()
    print("Números:", lista)
    print("Media:", f"{media(lista):.2f}")
    print("Mayor:", f"{mayor(lista):.2f}")

