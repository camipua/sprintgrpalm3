#FUNCIONES

def agregar_cliente(clientes, id, nombre, apellido, edad, contraseña):
    nuevo_cliente = {'ID': id, 'nombre': nombre, 'apellido': apellido, 'edad': edad, 'contraseña': contraseña}
    clientes.append(nuevo_cliente)
    
def eliminar_cliente(clientes, id):
    for cliente in clientes:
        if cliente['ID'] == id:
            clientes.remove(cliente)
            break
            
def mostrar_clientes(clientes):
    for cliente in clientes:
        print(f"ID: {cliente['ID']}, nombre: {cliente['nombre']}, apellido: {cliente['apellido']}, edad: {cliente['edad']}, contraseña: {cliente['contraseña']}")


# LISTA DE CLIENTES

clientes = [
    {'ID': 1, 'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 30, 'contraseña': '1234'},
    {'ID': 2, 'nombre': 'María', 'apellido': 'González', 'edad': 25, 'contraseña': '5678'},
    {'ID': 3, 'nombre': 'Pedro', 'apellido': 'Rodríguez', 'edad': 35, 'contraseña': 'abcd'},
    {'ID': 4, 'nombre': 'Laura', 'apellido': 'López', 'edad': 28, 'contraseña': 'efgh'}
]

# MENÚ INTERACCIÓN USUARIO

while True:
    print("Elija una opción:")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar todos los clientes")
    print("4. Salir")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        id = int(input("Ingrese el ID del nuevo cliente: "))
        nombre = input("Ingrese el nombre del nuevo cliente: ")
        apellido = input("Ingrese el apellido del nuevo cliente: ")
        edad = int(input("Ingrese la edad del nuevo cliente: "))
        contraseña = input("Ingrese la contraseña del nuevo cliente: ")
        agregar_cliente(clientes, id, nombre, apellido, edad, contraseña)
        print("Nuevo cliente agregado!")
    
    elif opcion == "2":
        id = int(input("Ingrese el ID del cliente a eliminar: "))
        eliminar_cliente(clientes, id)
        print("Cliente eliminado")
        
    elif opcion == "3":
        mostrar_clientes(clientes)
    
    elif opcion == "4":
        break
    
    else:
        print("Opción inválida. Intente de nuevo.")
