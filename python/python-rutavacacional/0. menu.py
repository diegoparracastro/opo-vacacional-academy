def gestion_vuelo():
    # Lógica para la gestión de vuelo
    print("Gestión de vuelo")

def gestion_login():
    # Lógica para la gestión de login
    print("Gestión de login")

def gestion_transporte():
    # Lógica para la gestión de transporte
    print("Gestión de transporte")

def gestion_pago():
    # Lógica para la gestión de pago
    print("Gestión de pago")

def gestion_reserva():
    # Lógica para la gestión de reserva
    print("Gestión de reserva")

def gestion_hotel():
    # Lógica para la gestión de hotel
    print("Gestión de hotel")

def carrito_compras():
    # Lógica para el carrito de compras
    print("Carrito de compras")

def mostrar_menu():
    print("== Menú de Turismo ==")
    print("1. Gestión de Vuelo")
    print("2. Gestión de Login")
    print("3. Gestión de Transporte")
    print("4. Gestión de Pago")
    print("5. Gestión de Reserva")
    print("6. Gestión de Hotel")
    print("7. Carrito de Compras")
    print("8. Salir")

opciones = {
    1: gestion_vuelo,
    2: gestion_login,
    3: gestion_transporte,
    4: gestion_pago,
    5: gestion_reserva,
    6: gestion_hotel,
    7: carrito_compras,
    8: exit
}

while True:
    mostrar_menu()
    opcion = int(input("Selecciona una opción: "))

    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")