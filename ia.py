#minimax apliaccion
print("global")

def minimax(juego ,quien_juega, profundidad):
    #si la profundidad es 0 se calcula su puntiacion
    pass

def funcion_utilidad(juego):
    negro = 0
    blanco = 0
    for i in juego:
        for j in i:
            if(j == 1):
                negro = negro + 1
            elif (j == 2):
                blanco = blanco + 1
    res = negro - blanco
    return res


def funcion_evaluacion(juego, jugadas_posibles, quien_juega, profundidad):
    if(profundidad == 0):
        valor = funcion_utilidad(juego)
        if valor < 0:
            return 100
        elif valor > 0:
            return -100
        else:
            return 0    
    #recorrer tabla con posibles jugadas
    if(quien_juega == 1):
        valor = 100
    else:
        valor = -100
    aux = 0
    for i in juego:
        for j in i:
            #entrega min (negro)
            if(quien_juega == 1):
                if(jugadas_posibles[i][j] == -(quien_juega)):
                    aux = Tablero.tabla_valorada[i][j]
                    if(aux < valor):
                        valor = aux
            #entrega max (blanco)
            elif(quien_juega == 2):
                if(jugadas_posibles[i][j] == -(quien_juega)):
                    aux = Tablero.tabla_valorada[i][j]
                    if(aux > valor):
                        valor = aux
    
    return valor