from Tablero import Tablero

if __name__ == "__main__":

    juego_nuevo = Tablero()
    for i in juego_nuevo.tabla:
        print(i)

    print("")

    juego_nuevo.movimiento_posible(2,2,2)
    juego_nuevo.movimiento_posible(3,3,2)
    
    for i in juego_nuevo.tabla:
        print(i)

        
    print("")

    juego_nuevo.limpia_tablero()
    juego_nuevo.jugada(1,3, 2)
    
    
    for i in juego_nuevo.tabla:
        print(i)


    juego_nuevo.movimiento_posible(3,2,1)
    print("")


    for i in juego_nuevo.tabla:
        print(i)

    juego_nuevo.limpia_tablero()
    juego_nuevo.jugada(3,4, 1)
    
    print("")


    for i in juego_nuevo.tabla:
        print(i)


    
    print("")


    for i in juego_nuevo.tabla:
        print(i)


    
    print("")