"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función que calculará el valor elevado al cuadrado y al cubo

de dicho número, puedes devolver un diccionario o una lista
- Utilizar el módulo math de python.
"""
from operaciones import cargar_valor, raiz_cuadrada, potencias

valor = cargar_valor()
print(f"Raíz cuadrada: {raiz_cuadrada(valor)}")

resultado = potencias(valor)
print(f"Cuadrado: {resultado['cuadrado']}")
print(f"Cubo: {resultado['cubo']}")
