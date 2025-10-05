"""
Crear una función que aceptará por parámetro dos valores que serán ingresados por el usuario, una lista donde los
valores serán llenados por el usuario también y un segundo parámetro que eliminará de la lista que fue ingresada a la
función, finalmente el output de la función será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado.
"""
def eliminar_de_lista(lista, valor):
    print("Lista original:", lista)
    if valor in lista:
        lista.remove(valor)
        print(f"Se eliminó el valor {valor}.")
    else:
        print(f"El valor {valor} no estaba en la lista.")
    return lista

lista_usuario = [1, 2, 3, 4, 5]
valor_a_eliminar = int(input("Ingrese un número a eliminar de la lista [1,2,3,4,5]: "))

lista_final = eliminar_de_lista(lista_usuario, valor_a_eliminar)
print("Lista final:", lista_final)