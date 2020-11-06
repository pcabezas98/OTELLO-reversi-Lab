from Tablero import Tablero
import copy
#minimax apliaccion
cantidad_de_repeticiones = 0

#funcion que muestra la cantidad de nodos que recorre
def mostrar():
    return cantidad_de_repeticiones

def minimax(juego ,quien_juega, ganador, oponente , profundidad):
    #si la profundidad es 0 se calcula su puntiacion
    #debe retornar una tupla que tiene la tabla y el Valor
    global cantidad_de_repeticiones
    cantidad_de_repeticiones = cantidad_de_repeticiones + 1
    
    if(profundidad == 0):
        resultado_1 = funcion_evaluacion(juego, quien_juega)
        return [resultado_1]

    #si el tablero esta en un nodo final me retorna quien gano
    if(juego.juego_terminado()):
        return [funcion_utilidad(juego, quien_juega)]
    if(quien_juega == 1):
        ficha_contraria = 2
    else:
        ficha_contraria = 1

    cantidad_de_caminos =  juego.cantidad_de_caminos(quien_juega)

    #pass
    if cantidad_de_caminos == 0:
        return minimax(juego, ficha_contraria,ganador ,oponente,profundidad)
    
    valor = []
    mejor_val = None
    mejor_movimiento = []
    #juego_nuevito = Tablero()
    #max
    if ganador == quien_juega:
        mov_posibles = juego.cordenadas_posibles_jugadas(quien_juega)
        for i in range(cantidad_de_caminos):
            cord_x = mov_posibles[i][0]
            cord_y = mov_posibles[i][1]
            juego_nuevito = copy.deepcopy(juego)
            juego_nuevito.aplica_jugada(cord_x,cord_y,quien_juega)
            valor = minimax(juego_nuevito,ficha_contraria, ganador, oponente, profundidad-1)
            if mejor_val == None or valor[0] > mejor_val:
                mejor_val = valor[0]
                mejor_movimiento = [cord_x,cord_y]
    #min
    if oponente == quien_juega:
        mov_posibles = juego.cordenadas_posibles_jugadas(quien_juega)
        for i in range(cantidad_de_caminos):
            cord_x = mov_posibles[i][0]
            cord_y = mov_posibles[i][1]
            juego_nuevito = copy.deepcopy(juego)
            juego_nuevito.aplica_jugada(cord_x,cord_y,quien_juega)
            valor = minimax(juego_nuevito,ficha_contraria, ganador, oponente, profundidad-1)
            
            if mejor_val == None or valor[0] < mejor_val:
                mejor_val = valor[0]
                mejor_movimiento = [cord_x,cord_y]


    return [mejor_val, mejor_movimiento]

def funcion_utilidad(juego, quien_juega):
    jugador = 0
    oponente = 0
    for i in range(6):
        for j in range(6):
            if(juego.tabla[i][j] == quien_juega):
                jugador = jugador + 1
            else:
                oponente = oponente + 1
    valor = jugador - oponente
    #si gana max
    if valor > 0:
        return 1000
    #si gana min
    elif valor < 0:
        return -1000
    #si empatan
    else:
        return 0   


def funcion_evaluacion(juego, quien_juega):
    #recorrer tabla con posibles jugadas
    juego.limpia_tablero()
    jugador = 0
    oponente = 0
    for i in range(6):
        for j in range(6):
            if(juego.tabla[i][j] == quien_juega):
                jugador = jugador + juego.tabla_valorada[i][j]
            elif(juego.tabla[i][j] != quien_juega and juego.tabla[i][j] != 0):
                oponente = oponente + juego.tabla_valorada[i][j]       
    salida = jugador - oponente

    return salida