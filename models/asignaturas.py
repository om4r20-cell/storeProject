"""
Clase Asignaturas
Fase 1: modelo inicial de una asignatura, asociada a un programa
academico (relacion de asociacion: Asignaturas -> Programa_academico).
"""


class asignaturas:
    def __init__(self, nombre, codigo, creditos, programa_academico):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos
        # Se guarda el objeto Programa_academico completo (asociacion),
        # no solo su nombre, para poder consultar cualquiera de sus datos.
        self._programa_academico = programa_academico

    def GetNombre(self):
        return self._nombre

    def SetNombre(self, nombre):
        self._nombre = nombre

    def GetCodigo(self):
        return self._codigo

    def SetCodigo(self, codigo):
        self._codigo = codigo

    def GetCreditos(self):
        return self._creditos

    def SetCreditos(self, creditos):
        self._creditos = creditos

    def GetPrograma_Academico(self):
        return self._programa_academico

    def SetPrograma_Academico(self, programa_academico):
        self._programa_academico = programa_academico

    def ShowInformation(self):
        """Presenta la informacion de la asignatura."""
        return (
            f"Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Creditos: {self._creditos} | "
            f"Programa: {self._programa_academico.GetNombre()}"
        )
