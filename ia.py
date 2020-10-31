#minimax apliaccion
print("global")

def minimax(juego ,quien_juega, profundidad):
    #si la profundidad es 0 se calcula su puntiacion
    if profundidad == 0:
        return funcion_evaluacion(juego[1])
    
    if profundidad == 0:
        return funcion_evaluacion()

    

       
        
        
def funcion_utilidad(juego, quien_juega):
    negro = 0
    blanco = 0
    for i in juego.tabla:
        for j in i:
            if(j == 1):
                negro = negro + 1
            elif (j == 2):
                blanco = blanco + 1
    return(negro, blanco)


def funcion_evaluacion(juego, quien_juega):
    if(juego.actualiza_movimientos(quien_juega) == 0):
        valor = funcion_utilidad(juego, quien_juega)
        
    for i in juego.tabla:
        for j in i:
            if(j == quien_juega):
                valor = juego.tabla_valorada[i][j]
    
    return valor