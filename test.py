from ia import *
from Tablero import Tablero


if __name__ == "__main__":
    juego_nuevo = Tablero()
    tabla = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,1,2,0,0],
             [0,0,2,1,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

    juego_nuevo.tabla = tabla
    #juego, quien juega, 1,2, profundidad
    cantidad_antes = mostrar()
    resultado = minimax(juego_nuevo, 1,1,2,3)
    cantidad_despues = mostrar()
    print(f"cantidad total : {cantidad_despues-cantidad_antes}")
    print(f"cantidad de nodos recorridos: {cantidad_despues}, \nmejor valor: {resultado[0]}, con cordenada {resultado[1]}")

    juego_nuevo.aplica_jugada(resultado[1][0],resultado[1][1],1)
    cantidad_antes = mostrar()
    resultado = minimax(juego_nuevo, 2,2,1,5)
    cantidad_despues = mostrar()
    print(f"\ncantidad total : {cantidad_despues-cantidad_antes}")
    print(f"cantidad de nodos recorridos: {cantidad_despues}, \nmejor valor: {resultado[0]}, con cordenada {resultado[1]}")

    juego_nuevo.aplica_jugada(resultado[1][0],resultado[1][1],2)
    cantidad_antes = mostrar()
    resultado = minimax(juego_nuevo, 1,1,2,6)
    cantidad_despues = mostrar()
    print(f"\ncantidad total : {cantidad_despues-cantidad_antes}")
    print(f"cantidad de nodos recorridos: {cantidad_despues}, \nmejor valor: {resultado[0]}, con cordenada {resultado[1]}")