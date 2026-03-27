
print("Bienvenido a la tienda")

opcion = input("¿Desea comprar un producto? (si/no): ").lower().strip()

if opcion == "si": 
    
    # Entrada de nombre
    nombre = input("Ingrese el nombre del producto: ")

    while True:
        precio = input("Ingrese el precio: ")
        
        if not precio.replace('.', '', 1).isdigit():
            print("Error: ingrese un número válido")
            continue
        
        precio = float(precio)
        
        if precio < 0:
            print("Error: el precio no puede ser negativo")
        else:
            break

    # Validar cantidad
    while True:
        cantidad = input("Ingrese la cantidad: ")
        
        if not cantidad.isdigit():
            print("Error: ingrese un número entero válido")
            continue
        
        cantidad = int(cantidad)
        
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa")
        else:
            break

    # Proceso
    costo_total = precio * cantidad

    # Salida
    print("\n--- RESULTADO ---")
    print(f"Producto: {nombre}")
    print(f"Precio: {precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Total: {costo_total}")

elif opcion == "no":
    print("Gracias por visitar la tienda")

else:
    print("Opción no válida")