print("Bienvenido a la Tienda Virtual")

# Opciones de menu.
opciones = ["Agregar productos al carrito", 
            "Ver carrito", 
            "Realiza el pago y salir"]



# Opciones de productos.
articulos = {"Camiseta": 20,
             "Jeans": 40,
             "Zapatos": 60,
             "Sombrero": 10,
             "Bolso": 30}

# Carrito de compras
carrito = []


while True:
    # Impresion de las opciones del menu.
    print("\nMenu:")
    print(f"1.{opciones[0]}\n2.{opciones[1]}\n3.{opciones[2]}")
    selec = input("Seleccione una opcion: ")
    # Impresion de la opciones de productos
    if selec == "1":
            print("\nProductos disponibles")
            [print(f"* {producto} ${precio}")for producto, precio in articulos.items()]
            comprar = input("Ingrese el nombre del producto que desea agregar: ").title()
            # agregar producto al carrito
            if comprar in articulos:
               carrito.append(comprar)
               print(f"Producto '{comprar}' agregado al carrito.")
    elif selec == "2":
         print("\nCarrito:")
         for producto3 in set(carrito):
              cantidad = carrito.count(producto3)
              precio_unitario = articulos[producto3]
              print(f"{cantidad} {producto3} - ${precio_unitario} c/u")
    elif selec == "3":
        total_a_pagar = sum(articulos[producto3] for producto3 in carrito)
        print(f"Total a pagar: ${total_a_pagar}")

        try:
             
             monto_pagado = float(input("Ingrese el monto con el que pagara: "))
             cambio = monto_pagado - total_a_pagar

             if cambio >= 0:
                  mensaje_cambio = f"Su cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requiere cambio."
                  print(f"Gracias por su compra. {mensaje_cambio}")
                  break
             else:
                  print("Monto invalido. por favor, ingrese un monto valido.")

        except Exception as e:
            print("Monto invalido por favor, ingrese un monto valido.")


    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")



    
        
        
    



