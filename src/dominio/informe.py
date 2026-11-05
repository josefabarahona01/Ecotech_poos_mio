class Informe:
    def __init__(self, id_informe: int, tipo_informe: str, contenido: str):
        self._id_informe = id_informe
        self._tipo_informe = tipo_informe
        self._contenido = contenido

    def exportar_pdf(self) -> None:
        pass

    def exportar_excel(self) -> None:
        pass