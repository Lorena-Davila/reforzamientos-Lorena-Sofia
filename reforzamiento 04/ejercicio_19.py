"""
Crear una función y dentro la respectiva excepción o excepciones para el siguiente bloque de código para que
tu programa no se bloquee, ya que solo aceptará datos tipos entero y además imprimir un mensaje al usuario
la causa y/o solución. También debe indicar el índice donde ingresarás este nuevo dato, si el índice está fuera
de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error
"""
lista = [2, 6, 10, 4, 5, 23, 1]

def insertar_en_lista(valor, indice):
    try:
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un número entero")
        lista[indice] = valor
        print("Lista actualizada:", lista)

    except IndexError:
        print("Error: índice", indice, "fuera de rango")
    except TypeError as error:
        print("Error:", error)
    finally:
        print("Operación finalizada\n")

insertar_en_lista(99, 2)

insertar_en_lista("texto", 3)

insertar_en_lista(50, 10)
