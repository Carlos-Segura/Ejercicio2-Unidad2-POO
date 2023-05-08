from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class ManejadorViajero():
    
    def __init__(self):
        self.__listaViajero = []
        
    def lecturaDeArchivo(self):
        archivo = open('ViajeroFrecuente.csv','r')
        reader = csv.reader(archivo, delimiter=';')
        
        for fila in archivo:
            print(fila)
            self.__listaViajero.append(fila)
        archivo.close()
        
        print("Esta es la lista...\n")
        print(self.__listaViajero)
        
    def menu(self):
        print("1. Consultar millas")
        print("2. Acumular millas")
        print("3. Canjear millas")            
        
    def menuOpciones(self, numViajero):
        i = 0
        while i > 0 and i < len(self.__listaViajero):
            if numViajero == self.__listaViajero[i]:
                ManejadorViajero.menu()
                opcion = int(input('Ingrese una opcion: '))
                match opcion:
                    case 1:
                        ViajeroFrecuente.cantidadTotalMillas()
                    case 2:
                        recorridas = int(input('Cantidad de millas a acumular: '))
                        ViajeroFrecuente.acumularMillas(recorridas)
                    case 3:
                        millas_a_canjear = int(input('Cantidad de millas a canjear: '))
                        ViajeroFrecuente.canjearMillas(millas_a_canjear)
                    case _:
                        print("Salió con exito!")
   
    def compararMayor(self):
        otro = ViajeroFrecuente.acumularMillas()
        if ViajeroFrecuente.__gt__(otro):
            print("El viajero " + ViajeroFrecuente.getNombre + " tiene mayor cantidad de millas acumuladas (", ViajeroFrecuente.acumularMillas, ").")
        else:
            print("El viajero " + ViajeroFrecuente.getNombre + " tiene mayor cantidad de millas acumuladas (", otro, ").")    
    
    def mayorCantidadMillas(self):
        otroViajero = self.__listaViajero
        ViajeroFrecuente.__gt__(otroViajero)