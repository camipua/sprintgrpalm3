import time

# Definición de funciones

def sumar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a sumar: "))
    productos[producto]["stock"] += cantidad
    print(f"Se agregaron {cantidad} unidades al stock de {producto}.")

def restar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a restar: "))
    if cantidad > productos[producto]["stock"]:
        print("No hay suficiente stock disponible para restar esa cantidad.")
    else:
        productos[producto]["stock"] -= cantidad
        print(f"Se restaron {cantidad} unidades del stock de {producto}.")

def agregar_producto():
    producto = input("Ingrese el nombre del nuevo producto: ")
    descripcion = input("Ingrese la descripción del nuevo producto: ")
    stock = int(input("Ingrese el stock inicial del nuevo producto: "))
    productos[producto] = {"stock": stock, "descripcion": descripcion}
    print(f"Se agregó el nuevo producto '{producto}' al inventario.")

def quitar_producto():
    producto = input("Ingrese el nombre del producto a quitar: ")
    if producto in productos:
        del productos[producto]
        print(f"Se quitó el producto '{producto}' del inventario.")
    else:
        print("El producto ingresado no existe en el inventario.")

def verificar_stock():
    for producto, datos in productos.items():
        if datos["stock"] < 400:
            print(f"ALERTA: El stock de {producto} es menor a 400 unidades. Actualmente hay {datos['stock']} unidades en stock.")

# bodega

productos = {
    "vasos": {'stock': 400, 'descripcion': 'lorem ipsum'},
    "cucharas": {'stock': 450, 'descripcion': 'lorem ipsum 2'},
    "cuchillos": {'stock': 350, 'descripcion': 'lorem ipsum 3'},
    "tenedores": {'stock': 400, 'descripcion': 'lorem ipsum 4'}
}

print("Bienvenido a bodega")
opcion = ""

while opcion != "salir":
    print("\nSeleccione una opción:")
    print("1. Sumar unidades de productos")
    print("2. Restar unidades de productos")
    print("3. Agregar nuevos productos")
    print("4. Quitar productos")
    print("5. Mostrar todos los productos y su stock")
    print("6. Verificar si hay productos con menos de 400 unidades")
    print("7. Salir")

    opcion = input("\nOpción seleccionada: ")

    if opcion == "1":
        sumar_producto()

    elif opcion == "2":
        restar_producto()

    elif opcion == "3":
        agregar_producto()

    elif opcion == "4":
        quitar_producto()

    elif opcion == "5":
        # Mostrar todos los productos y su stock con un desfase de un segundo entre cada producto
        for producto, datos in productos.items():
            print(f"{producto}: {datos['stock']} unidades - {datos['descripcion']}")
            time.sleep(1)

    elif opcion == "6":
        verificar_stock()
            
    elif opcion == "7":
        print("Hasta luego")
        opcion = "salir"

    else:
        print("Opción inválida, por favor seleccione una opción válida.")
