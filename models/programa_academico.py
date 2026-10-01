# Clase Programa_academico
# Representa un programa de la universidad (ej: Ingenieria de
# Sistemas), con sus datos basicos.
 
class Programa_academico:
    def __init__(self, nombre, codigo, facultad, numero_semestres, modalidad):
        self._nombre = nombre
        self._codigo = codigo
        self._facultad = facultad
        self._numero_semestres = numero_semestres
        self._modalidad = modalidad
 
    # Get y Set de nombre
    def GetNombre(self):
        return self._nombre
 
    def SetNombre(self, nombre):
        self._nombre = nombre
 
    # Get y Set de codigo
    def GetCodigo(self):
        return self._codigo
 
    def SetCodigo(self, codigo):
        self._codigo = codigo
 
    # Get y Set de facultad
    def GetFacultad(self):
        return self._facultad
 
    def SetFacultad(self, facultad):
        self._facultad = facultad
 
    # Get y Set de numero de semestres
    def GetNumero_Semestres(self):
        return self._numero_semestres
 
    def SetNumero_Semestres(self, numero_semestres):
        self._numero_semestres = numero_semestres
 
    # Get y Set de modalidad
    def GetModalidad(self):
        return self._modalidad
 
    def SetModalidad(self, modalidad):
        self._modalidad = modalidad
 
    def ShowInformation(self):
        # texto con todos los datos del programa, para verlo
        # completo en consola de una sola vez
        return (
            f"Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Facultad: {self._facultad} | "
            f"Semestres: {self._numero_semestres} | "
            f"Modalidad: {self._modalidad}"
        )