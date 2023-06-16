def iniciar():
    contraseña_correcta = "12345"
    usuario_correcto = "Gmail.com"

    contraseña = input("Por favor digite la contraseña: ")
    usuario = input("Por favor ingrese el usuario: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Ingreso exitoso")
    else:
        print("Ingreso inválido")

iniciar()