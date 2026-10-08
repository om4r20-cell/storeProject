class persona:
    def __init__(self, identificacion, Nombre, Correo):
        self.identificacion = identificacion #atributo para la identidad de la persona
        self.__Nombre = Nombre #atributo para el nombre de la persona
        self.Correo = Correo #atributo para el correo de la persona
        
        def getinformacion(self):
              return self.__indentificacion #retorna la identidad de la persona
        
        def getNombre(self):
            return self.__Nombre #retorna el nombre de la persona
        
        def getCorreo(self):
            return self.__Correo #retorna el correo de la persona
        
            @correo.setter
            def correo(self, valor):
                valor = validar_texto_no_vacio (valor, "correo electronico") #valida que el correo no esté vacío
                if "@" not in valor or valor.startswith("@") or valor.endswith("@"): #valida que el correo contenga un "@" y que no esté al inicio o al final del correo              
                    raise ValueError(f"El correo '{valor}' no es valido.")
                self.__Correo = valor #asigna un nuevo valor al correo de la persona
                
        def mostrar_informacion(self):
            return (f"Identificacion: {self.identificacion} | Nombre: {self.__Nombre} | Correo: {self.Correo}") #retorna la información de la persona en un formato legible
        
        def activida_principal(self):
            return f"{self.Nombre} es una persona vinculada a la universidad." #retorna la actividad principal
        
        def __str__(self):
            return self.mostrar_informacion() #retorna la información de la persona en un formato legible
        
        
        
    
        return self.__Nombre #retorna el nombre de la persona
    
    
    
    
        