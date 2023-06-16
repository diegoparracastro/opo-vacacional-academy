hoteles = {}

def obtener_input(mensaje):
    return input(mensaje + ": ")

def registrar_hotel():
    nombre = obtener_input("Ingrese el nombre del hotel")
    direccion = obtener_input("Ingrese la dirección del hotel")
    telefono = obtener_input("Ingrese el número de teléfono del hotel")

    # Crear un nuevo diccionario para el hotel
    hotel = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono
    }

    # Agregar el hotel al diccionario general de hoteles
    hoteles[nombre] = hotel

    print("¡Registro exitoso!")

def buscar_hotel():
    nombre = obtener_input("Ingrese el nombre del hotel")

    # Verificar si el hotel existe en el diccionario de hoteles
    if nombre in hoteles:
        hotel = hoteles[nombre]
        print("Información del hotel:")
        print("Nombre:", hotel['nombre'])
        print("Dirección:", hotel['direccion'])
        print("Teléfono:", hotel['telefono'])
    else:
        print("El hotel no está registrado")

# Ejemplo de uso
registrar_hotel()
buscar_hotel()
    