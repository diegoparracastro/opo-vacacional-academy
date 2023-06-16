# Diccionario para almacenar usuarios
usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    # Crear un nuevo diccionario para el usuario
    usuario = {
        'nombre': nombre,
        'correo': correo,
        'contraseña': contraseña
    }

    # Agregar el usuario al diccionario general de usuarios
    usuarios[correo] = usuario

    print("¡Registro exitoso!")

def iniciar_sesion():
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verificar si el correo existe en el diccionario de usuarios
    if correo in usuarios:
        usuario = usuarios[correo]

        # Verificar si la contraseña coincide
        if contraseña == usuario['contraseña']:
            print("¡Inicio de sesión exitoso!")
            print("Bienvenido,", usuario['nombre'])
        else:
            print("Contraseña incorrecta")
    else:
        print("El correo electrónico no está registrado")
  