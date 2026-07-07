"""
Programa principal del sistema Restaurante.

Este módulo permite interactuar con el usuario mediante
un menú de consola para gestionar productos y clientes.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n" + "=" * 40)
    print("      SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")


def registrar_producto(restaurante):
    """
    Registra un nuevo producto.
    """

    print("\n--- Registrar producto ---")

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))

    producto = Producto(nombre, categoria, precio)

    restaurante.agregar_producto(producto)

    print("\nProducto registrado correctamente.")


def listar_productos(restaurante):
    """
    Muestra todos los productos registrados.
    """

    print("\n--- Lista de productos ---")

    productos = restaurante.listar_productos()

    if productos:

        for producto in productos:
            print(producto.mostrar_informacion())

    else:
        print("No existen productos registrados.")


def buscar_producto(restaurante):
    """
    Busca un producto por su nombre.
    """

    print("\n--- Buscar producto ---")

    nombre = input("Ingrese el nombre del producto: ")

    producto = restaurante.buscar_producto(nombre)

    if producto:
        print("\nProducto encontrado:")
        print(producto.mostrar_informacion())
    else:
        print("\nNo se encontró el producto.")


def registrar_cliente(restaurante):
    """
    Registra un nuevo cliente.
    """

    print("\n--- Registrar cliente ---")

    nombre = input("Nombre: ")
    correo = input("Correo electrónico: ")
    id_cliente = int(input("ID del cliente: "))

    cliente = Cliente(nombre, correo, id_cliente)

    restaurante.agregar_cliente(cliente)

    print("\nCliente registrado correctamente.")


def listar_clientes(restaurante):
    """
    Muestra todos los clientes registrados.
    """

    print("\n--- Lista de clientes ---")

    clientes = restaurante.listar_clientes()

    if clientes:

        for cliente in clientes:
            print(cliente.mostrar_informacion())

    else:
        print("No existen clientes registrados.")


def buscar_cliente(restaurante):
    """
    Busca un cliente por su identificador.
    """

    print("\n--- Buscar cliente ---")

    id_cliente = int(input("Ingrese el ID del cliente: "))

    cliente = restaurante.buscar_cliente(id_cliente)

    if cliente:
        print("\nCliente encontrado:")
        print(cliente.mostrar_informacion())
    else:
        print("\nNo se encontró el cliente.")


def main():
    """
    Ejecuta el sistema Restaurante.
    """

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            registrar_cliente(restaurante)

        elif opcion == "5":
            listar_clientes(restaurante)

        elif opcion == "6":
            buscar_cliente(restaurante)

        elif opcion == "7":
            print("\nGracias por utilizar el sistema Restaurante.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()