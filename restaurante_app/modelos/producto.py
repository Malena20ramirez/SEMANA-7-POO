"""
Módulo que contiene la clase Libro.

Esta clase demuestra el uso del constructor tradicional (__init__),
@property y @setter.
"""

class Producto:
    """
    Representa un producto dentro del sistema de restaurante.
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        """
        Inicializa un nuevo producto.
        """

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._nombre = nuevo_nombre

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str):
        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        self._categoria = nueva_categoria

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self._precio = nuevo_precio

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool):
        self._disponible = estado

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del producto en formato legible.
        """

        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
        
