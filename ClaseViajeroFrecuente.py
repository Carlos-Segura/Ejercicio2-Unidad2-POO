class ViajeroFrecuente():
    
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
        
    def getNumero(self):
        return self.__num_viajero
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
        
    def retornaApe(self):
        return self.__apellido
        
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millasrecorridas):
        self.__add__(millasrecorridas)
        #self.__millas_acum = self.__millas_acum + millasrecorridas
        return self.cantidadTotalMillas()
    
    def canjearMillas(self, cant_canj):
        if cant_canj <= self.__millas_acum:
            self.__sub__(cant_canj)
            #self.__millas_acum = self.__millas_acum - cant_canj
        else:
            print("Operación erronea.")
        return self.__millas_acum
    
    def __gt__(self, otro):
        return self.__millas_acum > otro.cantidadTotalMillas()  
    
    def __add__(self, millasrecorridas):
        return self.__millas_acum + millasrecorridas
    
    def __sub__(self, otro):
        return self.__millas_acum - otro.canjearMillas()