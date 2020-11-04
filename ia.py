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
    #print(quien_juega)
    global cantidad_de_repeticiones
    cantidad_de_repeticiones = cantidad_de_repeticiones + 1
    #print(cantidad_de_repeticiones)
    if(profundidad == 0):
        resultado_1 = funcion_evaluacion(juego, quien_juega)
        return [resultado_1]
    #si el tablero esta en un nodo final me retorna quien gano

    if(juego.juego_terminado()):
        #print("terminaste")
        return [funcion_utilidad(juego, quien_juega)]
    if(quien_juega == 1):
        ficha_contraria = 2
    else:
        ficha_contraria = 1

    cantidad_de_caminos =  juego.cantidad_de_caminos(quien_juega)
    #print(f"cantidad_de_caminos: {cantidad_de_caminos}")
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
            #print(f"cordx:{cord_x}, cordy:{cord_y}, juega:{quien_juega}")
            juego_nuevito = copy.deepcopy(juego)
            juego_nuevito.aplica_jugada(cord_x,cord_y,quien_juega)
            #for i in juego.tabla:
            #    print(i)
            #print("")
            #for i in juego_nuevito.tabla:
            #    print(i)
            valor = minimax(juego_nuevito,ficha_contraria, ganador, oponente, profundidad-1)
            #print(f"evalua_:{valor[0]}")
            
            #print("valor 1")
            #print({valor[0]})
            #print("--------")
            #print("valor 2")
            #print({valor[1]})
            #print("--------")
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
            #print(f"evalua: {valor[0]}")
            
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

    
    #pos = {'max' : 0, "x" : 0, "y": 0}
    #max = -100
    #aux = 0
    #for i in range(6):
    #    for j in range(6):
    #        #entrega min (negro)
    #        if(juego.tabla[i][j] == -(quien_juega)):
    #            aux = juego.tabla_valorada[i][j]
    #            if(aux > max): 
    #                max = aux
    #                pos.update({'max' : max, "x" : i, "y": j})

            #entrega max (blanco)
            #if(juego.movimiento_posible[i][j] == -(quien_juega)):
            #    aux = Tablero.tabla_valorada[i][j]
            #    if(aux > valor):
            #        pos.append(valor)
            #        pos.append(i)
            #        pos.append(j)
    #
    return salida