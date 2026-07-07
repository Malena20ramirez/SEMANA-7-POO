"""
Módulo que contiene la clase Restaurante.

Esta clase administra los productos y clientes registrados
dentro del sistema de restaurante.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Administra los productos y clientes del sistema.
    """

    def __init__(self):
        """
        Inicializa las colecciones del sistema.
        """

        self.productos = []
        self.clientes = []

    # ==================================================
    # Métodos para gestionar productos
    # ==================================================

    def agregar_producto(self, producto: Producto):
        """
        Agrega un producto al restaurante.
        """

        self.productos.append(producto)

    def listar_productos(self):
        """
        Devuelve la lista de productos registrados.
        """

        return self.productos

    def buscar_producto(self, nombre: str):
        """
        Busca un producto por su nombre.
        """

        for producto in self.productos:

            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    # ==================================================
    # Métodos para gestionar usuarios
    # ==================================================

    def agregar_cliente(self, cliente: Cliente):
        """
        Agrega un cliente al restaurante.
        """

        self.clientes.append(cliente)

    def listar_clientes(self):
        """
        Devuelve la lista de clientes registrados.
        """

        return self.clientes

    def buscar_cliente(self, id_cliente: int):
        """
        Busca un cliente por su identificador.
        """

        for cliente in self.clientes:

            if cliente.id_cliente == id_cliente:
                return cliente

        return None