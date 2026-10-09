try:
    from .persona import persona
    from .validaciones import validar_texto_no_vacio, validar_entero_positivo
except ImportError:
    from persona import persona


class Docente(persona):
    HORAS_MAXIMAS_SEMANAlES = 168 #Horas que tiene una semana, para validar que no se exceda el limite de horas de trabajo
    def __init__(self, identificacion,nombre, correo, numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = validar_texto_no_vacio (numero_empleado, "Número de empleado") #Atributo para el numero de empleado del docente
        self.__facultad = facultad #Atributo para la facultad a la que pertenece el docente
        self.__tipo_contratacion = tipo_contratacion #Atributo para el tipo de contratación del docente
        self.__horas_semanales = horas_semanales #Atributo para las horas semanales del docente
        
    @property
    def numero_empleado(self):
        return self.__numero_empleado
    
    @property
    def facultad(self):
        return self.__facultad
    
    @facultad.setter
    def facultad(self, valor):
        self.__facultad = validar_texto_no_vacio(valor, "Facultad") #Valida que la facultad no sea vacia
        
    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion
    
    @tipo_contratacion.setter
    def tipo_contratacion(self, valor):
        self.__tipo_contratacion = validar_texto_no_vacio(valor, "Tipo de contratación") #Valida que el tipo de contratacion no sea vacio
        
    @property
    def horas_semanales(self):
        return self.__horas_semanales
    
    @horas_semanales.setter
    def horas_semanales(self, valor):
        valor = validar_entero_positivo(valor, "Horas semanales") #Valida que las horas semanales sean un entero positivo    
        if valor > self.HORAS_MAXIMAS_SEMANAlES:
            raise ValueError(f"Las horas semanales no pueden exceder {self.HORAS_MAXIMAS_SEMANAlES}.") #Valida que las horas semanales no excedan el limite de horas de trabajo
        self.__horas_semanales = valor
            
    def mostrar_informacion(self):
        return (f"[docente] {super ().mostrar_informacion()} | " 
                f"N° de empleado: {self.numero_empleado} | Facultad: {self.facultad} | "
                f"Contratacion: {self.tipo_contratacion} | "
                f"Horas semanales: {self.horas_semanales}")
        
    def actividad_principal(self):
        return f"{self.Nombre} el docente imparte clases en la facultad de {self.facultad}."
            
    
    