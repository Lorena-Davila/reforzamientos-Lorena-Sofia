"""
12. Escribe un programa que almacene información de un producto: Tu
nombre, nombre del producto, precio unitario (float), cantidad (int) e
imprimirá finalmente algo como lo siguiente:
Buen día Nombre, el detalle de su compra es el siguiente:
- Producto: Pollo a la brasa
- Precio unitario: 50.50
- Cantidad: 2
- Total a pagar: 101
"""
nombre = "Lorena"
producto = "Tablet Samsung Galaxy Tab S10 FE"
precio_unitario = 1549.00
cantidad = 2
total = precio_unitario * cantidad

print(f"Buen día {nombre}, el detalle de su compra es el siguiente:")
print(f"- Producto: {producto}")
print(f"- Precio unitario: {precio_unitario}")
print(f"- Cantidad: {cantidad}")
print(f"- Total a pagar: {total}")
