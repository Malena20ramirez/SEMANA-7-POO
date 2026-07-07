"""
Módulo que contiene la clase Usuario.

Esta clase demuestra el uso de @dataclass como una forma moderna
de crear automáticamente el constructor.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Representa un cliente dentro del sistema de restaurante.
    """

    nombre: str
    correo: str
    id_cliente: int

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información del cliente en formato legible.
        """

        return (
            f"ID: {self.id_cliente} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )