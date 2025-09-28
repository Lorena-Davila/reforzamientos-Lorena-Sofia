"""
Una empresa desea gestionar las facturas pendientes que tiene por pagar, para esto se creará un
diccionario donde tendrá por key el número de factura “00054” y su value será el coste de la factura.
El programa tendrá la opción de pedir nueva factura (por consola) que se agregará al diccionario.
Cada vez que el área de contabilidad pague una factura se pedirá el número de factura que fue cancelada,
si existe mostrar un mensaje donde indicará “La factura ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva factura se
mostrará inmediatamente al diccionario actualizado.
"""
facturas = {}

while True:
    opcion = input("\n1. Nueva factura\n2. Pagar factura\n3. Salir\nElige opción: ")

    if opcion == "1":
        numero_1 = input("Número de factura: ")
        costo = float(input("Costo: "))
        facturas[numero_1] = costo

    elif opcion == "2":
        numero_2 = input("Factura a pagar: ")
        if numero_2 in facturas:
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe")

    elif opcion == "3":
        break

    print("Facturas actuales:", facturas)


