# Diccionario para almacenar los productos
productos = {}

def agregar_producto():
    identificador = input("Ingrese el identificador del producto: ")
    if identificador in productos:
        print("Ese identificador ya existe. No se puede agregar.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        productos[identificador] = nombre
        print("Producto agregado correctamente.")

def actualizar_producto():
    identificador = input("Ingrese el identificador del producto a actualizar: ")
    if identificador in productos:
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        productos[identificador] = nuevo_nombre
        print("Producto actualizado correctamente.")
    else:
        print("El identificador no existe.")

def eliminar_producto():
    identificador = input("Ingrese el identificador del producto a eliminar: ")
    if identificador in productos:
        del productos[identificador]
        print("Producto eliminado correctamente.")
    else:
        print("El identificador no existe.")

def consultar_producto():
    identificador = input("Ingrese el identificador del producto a consultar: ")
    if identificador in productos:
        print(f"Nombre del producto: {productos[identificador]}")
    else:
        print("El identificador no existe.")

def mostrar_menu():
    print("\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Consultar producto")
    print("5. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        consultar_producto()
    elif opcion == "5":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción invalida. Intente de nuevo.")
