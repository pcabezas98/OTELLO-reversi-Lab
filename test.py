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
    resultado = minimax(juego_nuevo, 1,1,2,7)
    cantidad = mostrar()
    print(f"cantidad de nodos recorridos: {cantidad}, \nmejor valor: {resultado[0]}, con cordenada {resultado[1]}")
    