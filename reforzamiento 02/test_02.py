"""
2.Crea una variable tipo int. Luego, multiplica por 10 y restarle el valor de
10. Debes hacer todo esto en dos pasos. Finalmente convertirlo a float y
mostrar el resultado por pantalla y el tipo de variable también.
"""""
numero = 25
numero = numero * 10
numero = numero - 10
numero = float(numero)
print("Resultado:",numero)
print("Tipo de variable:",type(numero))