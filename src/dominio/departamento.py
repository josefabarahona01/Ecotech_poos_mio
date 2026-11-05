from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.dominio.empleado import Empleado

class Departamento:
    def __init__(self, id_departamento: int, nombre_departamento: str, gerente_cargo: str):
        self._id_departamento = id_departamento
        self._nombre_departamento = nombre_departamento
        self._gerente_cargo = gerente_cargo
        self._empleados: list[Empleado] = []  # Asociación con Empleado (multiplicidad 0..*)[cite: 29]

    def agregar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False  # Evita duplicados en la colección[cite: 29]
        self._empleados.append(empleado)
        return True

    def remover_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            return True
        return False

    @property
    def empleados(self) -> tuple[Empleado, ...]:
        return tuple(self._empleados)  # Vista inmutable para proteger el estado interno[cite: 31]