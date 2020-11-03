from Tablero import Tablero
#minimax apliaccion
##class nodo:
##    def __init__(self, profundidad, juegador, ramas_restantes, valor = 0):
##        self.profundidad = profundidad
##        self.juegador = juegador
##        self.ramas_restantes = ramas_restantes
##        self.valor = valor
##        self.hijo = []
##        self.creahijo()
##
##    def creahijo(self):
        

def minimax(juego ,quien_juega, profundidad):
    #si la profundidad es 0 se calcula su puntiacion
    #debe retornar una tupla que tiene la tabla y el Valor
    pass

def funcion_utilidad(juego, quien_juega):
    jugador = 0
    oponente = 0
    for i in range(6):
        for j in range(6):
            if(juego.tabla[i][j] == quien_juega):
                jugador = jugador + 1
            else:
                oponente = oponente + 1
    resultado = jugador - oponente
    return resultado


def funcion_evaluacion(juego, quien_juega):
    #si el tablero esta en un nodo final me retorna quien gano
    lleno = True
    for i in range(6):
        for j in range(6):
            if(juego.tabla[i][j] == 0):
                lleno = False

    if(lleno == True):
        valor = funcion_utilidad(juego, quien_juega)
        #si gana max
        if valor > 0:
            return 1000
        #si gana min
        elif valor < 0:
            return -1000
        #si empatan
        else:
            return 0    
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