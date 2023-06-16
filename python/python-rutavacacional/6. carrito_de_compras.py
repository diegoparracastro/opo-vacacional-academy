# Datos de transporte
transportes = ["Autobús", "Minibús", "Microbús"]
# Datos de hoteles
hoteles = ["Hotel A", "Hotel B", "Hotel C"]
# Datos de vuelos
vuelos = ["Vuelo 1", "Vuelo 2", "Vuelo 3"]

carrito = []

def mostrar_menu():
    print("== Menú de Carrito de Compras ==")
    print("1. Reservar Transporte")
    print("2. Reservar Hotel")
    print("3. Reservar Vuelo")
    print("4. Seleccionar Método de Pago")
    print("5. Mostrar Carrito")
    print("6. Salir")

def reservar_transporte():
    print("== Reserva de Transporte ==")
    for i, transporte in enumerate(transportes):
        print(f"{i+1}. {transporte}")

    opcion = int(input("Seleccione un transporte: "))
    transporte_seleccionado = transportes[opcion - 1]
    carrito.append(transporte_seleccionado)
    print(f"{transporte_seleccionado} agregado al carrito.")

def reservar_hotel():
    print("== Reserva de Hotel ==")
    for i, hotel in enumerate(hoteles):
        print(f"{i+1}. {hotel}")

    opcion = int(input("Seleccione un hotel: "))
    hotel_seleccionado = hoteles[opcion - 1]
    carrito.append(hotel_seleccionado)
    print(f"{hotel_seleccionado} agregado al carrito.")

def reservar_vuelo():
    print("== Reserva de Vuelo ==")
    for i, vuelo in enumerate(vuelos):
        print(f"{i+1}. {vuelo}")

    opcion = int(input("Seleccione un vuelo: "))
    vuelo_seleccionado = vuelos[opcion - 1]
    carrito.append(vuelo_seleccionado)
    print(f"{vuelo_seleccionado} agregado al carrito.")

def seleccionar_metodo_pago():
    print("== Selección de Método de Pago ==")
    metodo_pago = input("Ingrese el método de pago: ")
    carrito.append(metodo_pago)
    print(f"Método de pago '{metodo_pago}' agregado al carrito.")

def mostrar_carrito():
    print("== Carrito de Compras ==")
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        for item in carrito:
            print("- " + item)

while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if   opcion == 1:
        reservar_transporte()
    elif opcion == 2:
        reservar_hotel()
    elif opcion == 3:
        reservar_vuelo()
    elif opcion == 4:
        seleccionar_metodo_pago()
    elif opcion == 5:
        mostrar_carrito()
    elif opcion == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")