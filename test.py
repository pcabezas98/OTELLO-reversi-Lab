from ia import *
from Tablero import Tablero


if __name__ == "__main__":
    juego_nuevo = Tablero()
    tabla = [[2,0,0,0,0,1],
             [0,0,0,0,1,0],
             [0,0,2,1,0,0],
             [0,0,1,2,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

    juego_nuevo.tabla = tabla
    print(funcion_evaluacion(juego_nuevo, 2))
    