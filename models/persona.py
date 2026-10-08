def validar_texto_no_vacio(valor, campo):
    if valor is None or not str(valor).strip():
        raise ValueError(f"El {campo} no puede estar vacío.")
    return str(valor).strip()

class persona:
    def __init__(self, identificacion, Nombre, Correo):
        self.identificacion = identificacion #Atributo para la identidad de la persona
        self.Nombre = Nombre #Atributo para el nombre de la persona
        self.Correo = Correo #Atributo para el correo electrónico de la persona

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        self.__identificacion = validar_texto_no_vacio(valor, "identificacion") #Valida que la identificacion no sea vacia

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self, valor):
        self.__Nombre = validar_texto_no_vacio(valor, "nombre") #Valida que el nombre no sea vacio

    @property
    def Correo(self):
        return self.__Correo

    @Correo.setter
    def Correo(self, valor):
        valor = validar_texto_no_vacio(valor, "correo electronico")
        if "@" not in valor or valor.startswith("@") or valor.endswith("@"):
            raise ValueError(f"El correo '{valor}' no es valido.") #Valida que el correo tenga un formato correcto
        self.__Correo = valor

    def getidentificacion(self):
        return self.identificacion

    def getNombre(self):
        return self.Nombre

    def getCorreo(self):
        return self.Correo

    def mostrar_informacion(self):
        return f"Identificacion: {self.identificacion} | Nombre: {self.__Nombre} | Correo: {self.Correo}"

    def actividad_principal(self):
        return f"{self.Nombre} es una persona vinculada a la universidad."

    def __str__(self):
        return self.mostrar_informacion()
        
