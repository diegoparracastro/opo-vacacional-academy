def iniciar():
    contraseña_correcta = "12345"
    usuario_correcto = "Gmail.com"

    contraseña = input("Por favor digite la contraseña: ")
    usuario = input("Por favor ingrese el usuario: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Ingreso exitoso")
        cambiar_contraseña = input("¿Desea cambiar su contraseña? (S/N): ")
        
        if cambiar_contraseña.lower() == "s":
            nueva_contraseña = input("Por favor ingrese la nueva contraseña: ")
            contraseña_correcta = nueva_contraseña
            print("Contraseña cambiada exitosamente")
    else:
        print("Ingreso inválido")

iniciar()