from ManejadorClaseViajeroFrecuente import ManejadorViajero

if __name__ == '__main__':

    manejador = ManejadorViajero()
    manejador.lecturaDeArchivo()
    numViajero = int(input("Ingrese numero de viajero frecuente: "))
    manejador.menuOpciones(numViajero)
    manejador.mayorCantidadMillas()
    
