from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.dominio.registro_tiempo import RegistroTiempo

class Empleado:
    def __init__(self, id_persona: int, nombre: str, direccion: str, telefono: str, correo: str,
                id_empleado: int, fecha_contrato: date, salario_cifrado: str, password_hash: str, rol: str):
        # Atributos que antes pertenecían a Persona, ahora integrados directamente
        self._id_persona = id_persona
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._id_empleado = id_empleado
        self._fecha_contrato = fecha_contrato
        self.__salario_cifrado = salario_cifrado    
        self.__password_hash = password_hash        
        self._rol = rol
        self._registros_tiempo: list[RegistroTiempo] = []  # Relación de composición estricta

    def obtener_datos(self) -> str:
        return f"ID: {self._id_persona} | Nombre: {self._nombre} | Correo: {self._correo}"

    def autenticar(self, password_pass: str) -> bool:
        return self.__password_hash == password_pass

    def registrar_tiempo(self, proyecto, horas: float, desc: str) -> RegistroTiempo:
        from src.dominio.registro_tiempo import RegistroTiempo
        nuevo_registro = RegistroTiempo(
            id_registro=len(self._registros_tiempo) + 1,
            fecha=date.today(),
            horas_trabajadas=horas,
            descripcion_tarea=desc,
            empleado=self,
            proyecto=proyecto
        )
        self._registros_tiempo.append(nuevo_registro)
        return nuevo_registro