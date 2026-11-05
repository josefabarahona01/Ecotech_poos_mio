from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.dominio.empleado import Empleado
    from src.dominio.proyecto import Proyecto

class RegistroTiempo:
    def __init__(self, id_registro: int, fecha: date, horas_trabajadas: float, descripcion_tarea: str, empleado: Empleado, proyecto: Proyecto):
        self._id_registro = id_registro
        self._fecha = fecha
        self._horas_trabajadas = horas_trabajadas
        self._descripcion_tarea = descripcion_tarea
        self._empleado = empleado
        self._proyecto = proyecto

    def validar_entrada(self) -> bool:
        return self._horas_trabajadas > 0 and len(self._descripcion_tarea.strip()) > 0