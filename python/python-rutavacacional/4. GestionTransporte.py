# Datos de transporte
transportes = {
    "flota": ["Autobús", "Minibús", "Microbús"],
    "aerovans": ["Van ejecutiva", "Van VIP", "Van turística"],
    "taxi": ["Taxi regular", "Taxi de lujo", "Taxi compartido"]

}

# Base de datos de usuarios registrados (solo para fines de ejemplo)
usuarios_registrados = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

def gestion_transporte():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verificar las credenciales del usuario
    if verificar_credenciales(usuario, contraseña):
        print("Inicio de sesión exitoso.")
        mostrar_opciones_transporte(usuario)
    else:
        print("Credenciales inválidas. Vuelva a intentarlo.")

def verificar_credenciales(usuario, contraseña):
    # Verificar las credenciales del usuario en la base de datos
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        return True
    return False

def mostrar_opciones_transporte(usuario):
    while True:
        print("== Opciones de transporte ==")
        print("1. Flota")
        print("2. Aerovans")
        print("3. Taxi")
        print("4. reserva")
        print("5. Salir")

        opcion = int(input("Seleccione un tipo de transporte: "))

        if opcion == 1:
            print("Transporte seleccionado: Flota")
            gestion_flota(usuario)
        elif opcion == 2:
            print("Transporte seleccionado: Aerovans")
            gestion_aerovans(usuario)
        elif opcion == 3:
            print("Transporte seleccionado: Taxi")
            gestion_taxi(usuario)
        elif opcion == 4:
            print("reserva")
        elif opcion == 5:
            print("selecciono salir")
            break
        else:
    
            print("Opción inválida. Vuelva a intentarlo.")
        


def gestion_flota(usuario):
    # Lógica para gestionar la elección de transporte de flota
    print(f"Opciones de flota para el usuario {usuario}:")
    for transporte in transportes["flota"]:
        print("- " + transporte)
    # Otras operaciones relacionadas con la gestión de flota

def gestion_aerovans(usuario):
    # Lógica para gestionar la elección de transporte de aerovans
    print(f"Opciones de aerovans para el usuario {usuario}:")
    for transporte in transportes["aerovans"]:
        print("- " + transporte)
    # Otras operaciones relacionadas con la gestión de aerovans

def gestion_taxi(usuario):
    # Lógica para gestionar la elección de transporte de taxi
    print(f"Opciones de taxi para el usuario {usuario}:")
    for transporte in transportes["taxi"]:
        print("- " + transporte)
    # Otras operaciones relacionadas con la gestión de taxi
  
def gestio_reservas(usuario):
        print(f" El usuario reserva transporte {usuario}:")
  
gestion_transporte()