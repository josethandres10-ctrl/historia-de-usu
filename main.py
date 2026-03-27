print("bienvenido a la tienda virtual") 
historial = {}
pregunta = input("Para inciar el registro de una nueva venta, escriba 'si': ").strip().lower()
status = ("si", "yes")
while pregunta in status : #while ciclo repetitivo, se ejecuta mientras la condición sea verdadera, en este caso, mientras la variable pregunta sea igual a "si" o "yes"    
    total_valor = 0
    try:      
        producto = input("ingrese el nombre del producto: ")
        precio = int(input("ingrese el precio del producto: "))
        cantidad = int(input("ingrese la cantidad del producto: "))
        total = precio * cantidad
        historial[producto] = {"precio": precio, "cantidad": cantidad, "total": total} 
        total_valor += historial[producto]["total"]
        pregunta = input("¿desea comprar otro producto? (si/no): ").lower()
        if pregunta == "no" or pregunta == "nope":
            print(f"el total a pagar por {cantidad} {producto} es: {total} and el valor total de su compra es: {total_valor}")
            print("gracias por su compra, vuelva pronto")
            break
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el precio y la cantidad. Producto no registrado.")

print(("Fin del programa"))
print("Historial de compras:")
for producto, detalles in historial.items():
    print(f"Producto: {producto}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}, Total: {detalles['total']}")  



