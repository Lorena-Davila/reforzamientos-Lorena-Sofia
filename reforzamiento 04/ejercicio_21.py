"""
Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una excepción para el siguiente bloque de código
y tu programa no se bloquee. Además, imprime un mensaje al usuario la causa y/o solución (Pedir nombre, día, mes, año
por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes y año: No debe recibir un dato string,
sino decírselo al usuario
cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025
Independientemente del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error
"""
def saluda_fecha(nombre, dia, mes, anio):
    try:
        if nombre.isdigit():
            print("Error: el nombre no debe ser numérico")
            return

        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        print("Hello {}, hoy estamos {} de {} del {}".format(nombre, dia, mes, anio))

    except ValueError:
        print("Error: día, mes o año deben ser numéricos")

    finally:
        print("Operación finalizada")

saluda_fecha("Lorena", 27, 9, 2025)
saluda_fecha("101101", 27, 9, 2025)
saluda_fecha("Lorena", 27, "septiembre", 2025)
