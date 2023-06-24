vuelos = {
    "ejecutivo": ["con extras", "sin extras", "primera clase"],
    "comercial": ["programados", "temporada alta", "temporada baja"],
    "charter": ["con patron", "sin patron"],
    "economico_flexible": ["linea1", "linea2", "linea3"]

}

# Base de datos de usuarios registrados (solo para fines de ejemplo)
usuarios_registrados = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

def gestion_vuelo():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verificar las credenciales del usuario
    if verificar_credenciales(usuario, contraseña):
        print("Inicio de sesión exitoso.")
        mostrar_opciones_vuelo(usuario)
    else:
        print("Credenciales inválidas. Vuelva a intentarlo.")

def verificar_credenciales(usuario, contraseña):
    # Verificar las credenciales del usuario en la base de datos
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        return True
    return False

def mostrar_opciones_vuelo(usuario):
    while True:
        print("== Opciones de vuelos ==")
        print("1. ejecutivo")
        print("2. comercial")
        print("3. charter")
        print("4. economica flexible")
        print("5. Salir")

        opcion = int(input("Seleccione un tipo de vuelo: "))

        if opcion == 1:
            print("vuelo seleccionado: ejecutivo")
            gestion_ejecutivo(usuario)
        elif opcion == 2:
            print("vuelo seleccionado: comercial")
            gestion_comercial(usuario)        
        elif opcion == 3:
            print("vuelo seleccionado: charter")
            gestion_charter(usuario)
        elif opcion == 4:
            print("economica flexibre")
            gestion_economico_flexible(usuario)
        elif opcion == 5:
            print("selecciono salir")
            break
        else:
    
            print("Opción inválida. Vuelva a intentarlo.")
        


def gestion_ejecutivo(usuario):
    # Lógica para gestionar la elección de vuelo de ejecutivo
    print(f"Opciones de ejecutivo para el usuario {usuario}:")
    for vuelo in vuelos["ejecutivo"]:
        print("- " + vuelo)
    # Otras operaciones relacionadas con la gestión de ejecutivo

def gestion_charter(usuario):
    # Lógica para gestionar la elección de vuelo de charter
    print(f"Opciones de charter para el usuario {usuario}:")
    for vuelo in vuelos["charter"]:
        print("- " + vuelo)
    # Otras operaciones relacionadas con la gestión de charter

def gestion_economico_flexible(usuario):
    # Lógica para gestionar la elección de vuelo de economico flexible
    print(f"Opciones de economico flexible para el usuario {usuario}:")
    for vuelo in vuelos["economico flexible"]:
        print("- " + vuelo)
    # Otras operaciones relacionadas con la gestión de economico flexible
  
def gestion_comercial(usuario):
    # Lógica para gestionar la elección de vuelo de comercial
    print(f"Opciones de comercial para el usuario {usuario}:")
    for vuelo in vuelos["comercial"]:
        print("- " + vuelo)
    # Otras operaciones relacionadas con la gestion de comercial
  
gestion_vuelo()