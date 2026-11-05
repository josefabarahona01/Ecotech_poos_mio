from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.dominio.empleado import Empleado

class Proyecto:
    def __init__(self, id_proyecto: int, nombre_proyecto: str, descripcion: str, fecha_inicio: date):
        self._id_proyecto = id_proyecto
        self._nombre_proyecto = nombre_proyecto
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._empleados_asignados: list[Empleado] = []

    def asignar_empleado(self, empleado: Empleado) -> bool:
        if empleado not in self._empleados_asignados:
            self._empleados_asignados.append(empleado)
            return True
        return False

    def desasignar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados_asignados:
            self._empleados_asignados.remove(empleado)
            return True
        return False

    @property
    def empleados_asignados(self) -> tuple[Empleado, ...]:
        return tuple(self._empleados_asignados)