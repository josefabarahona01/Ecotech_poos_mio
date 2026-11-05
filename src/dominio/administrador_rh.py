from datetime import date
from src.dominio.empleado import Empleado
from src.dominio.departamento import Departamento
from src.dominio.informe import Informe

class AdministradorRH(Empleado):
    def __init__(self, id_persona: int, nombre: str, direccion: str, telefono: str, correo: str,
                id_empleado: int, fecha_contrato: date, salario_cifrado: str, password_hash: str, rol: str,
                nivel_acceso: str):
        super().__init__(id_persona, nombre, direccion, telefono, correo, id_empleado, fecha_contrato, salario_cifrado, password_hash, rol)
        self._nivel_acceso = nivel_acceso

    def registrar_empleado(self, e: Empleado) -> bool:
        return True

    def reasignar_departamento(self, e: Empleado, d: Departamento) -> bool:
        return True

    def generar_reporte(self, tipo: str) -> Informe:
        return Informe(id_informe=1, tipo_informe=tipo, contenido="Datos consolidados de gestión interna")