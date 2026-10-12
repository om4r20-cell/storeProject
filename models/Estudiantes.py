from .persona import persona
from .programa_academico import programa_academico
from .validaciones import validar_texto_no_vacio, validar_entero_positivo

class estudiante(persona):
    PROMEDIO MINIMO = 0.0
    PROMEDIO MAXIMO = 5.0 #ESCALA COLOMBIANA
    
    def __init__(self, identificacion, nombre, correo, codigo_estudiante, programa_academico, semestre, promedio_acumulado):
        super().__init__(identificacion, nombre, correo)
        self ._codigo_estudiante = validar_texto_no_vacio(codigo_estudiante, "Código de estudiante") #Atributo para el código del estudiante
        self ._programa_academico = programa_academico 
        self ._semestre = validar_entero_positivo(semestre, "Semestre") 
        self ._promedio_acumulado = self.validar_promedio(promedio_acumulado) 
    
    @property
    def codigo_estudiante(self):
        return self ._codigo_estudiante
    
    @property
    def programa_academico(self):
        return self ._programa_academico
    
    @programa_academico.setter
    def programa_academico(self, valor):
        if not isinstance(valor, programa_academico):
            raise ValueError("El programa académico debe ser una instancia de la clase programa_academico.") #Valida que el programa academico sea una instancia de la clase programa_academico
        self ._programa_academico = valor
        
    @property
    def semestre(self):
        return self ._semestre
    
    @semestre.setter
    def semestre(self, valor):
        valor = validar_entero_positivo(valor, "Semestre") #Valida que el semestre sea un entero positivo
        if valor > self.programa.numero_semestres:
            raise ValueError("El semestre {valor} excede los " 
                             f"{self.programa.numero_semestres} semestres del programa .") #Valida que el semestre no exceda el numero de semestres del programa academico
        self ._semestre = valor
        
    @property
    def promedio_acumulado(self):
        return self ._promedio_acumulado
    
    @promedio_acumulado.setter
    def promedio_acumulado(self, valor):
        if isinstance (valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("El promedio acumulado debe ser un número.") #Valida que el promedio acumulado sea un numero
        if not self.PROMEDIO_MINIMO <= valor <= self.PROMEDIO_MAXIMO:
            raise ValueError(f"El promedio acumulado debe estar entre {self.PROMEDIO_MINIMO} y {self.PROMEDIO_MAXIMO}.") #Valida que el promedio acumulado este entre el minimo y maximo
        self.__promedio_acumulado = float(valor)
        

#--------------------#
def mostrar_informacion(self):
    return (f"[estudiante] {super().mostrar_informacion()} | "
            f"Código: {self.codigo_estudiante} | Programa: {self.programa_academico.nombre} | "
            f"Semestre: {self.semestre} | Promedio acumulado: {self.promedio_acumulado}")
    
def actividad_principal(self):
    return f"{self.Nombre} cursa el programa de {self.programa_academico.nombre} y se encunetra en el semestre {self.semestre}."
