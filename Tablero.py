#from ia import ia

#negra = 1 "f_negra"
#blanca = 2 "f_blanca"
#camino = 0
#jugada posible negra = -1 "pos_negra"
#jugada posible blanca = -2 "pos_blanca"
class Tablero:
    x = 0
    y = 0
    tabla = [[]]
    tabla_simulada = [[]]
    tabla_valorada = [
        [100,  -10,  3,  3, -10, 100],
        [-10,  -20, -3, -3, -20, -10],
          [3,   -3,  1,  1, -3,   3],
          [3,   -3,  1,  1, -3,   3],
        [-10,  -20, -3, -3, -20, -10],
        [100,  -10,  3,  3, -10, 100]
    ]


    def __init__(self):
        self.x = 6
        self.y = 6
        self.f_negra = 1
        self.f_blanca = 2
        self.pos_negra = -1
        self.pos_blanca = -2

        self.tabla = [[0 for i in range(self.x)] for i in range(self.y)]
                
        self.tabla[2][2] = self.f_blanca
        self.tabla[3][3] = self.f_blanca
        self.tabla[3][2] = self.f_negra
        self.tabla[2][3] = self.f_negra

    def ganador(self):
        negro = 0
        blanco = 0
        for i in range(6):
            for j in range(6):
                if(self.tabla[i][j] == 1):
                    negro = negro + 1
                elif(self.tabla[i][j] == 2):
                    blanco = blanco + 1
        if(negro > blanco):
            return {"ganador": "Negras", "puntaje negro": negro, "puntaje blanco": blanco}
        if(negro < blanco):
            return {"ganador": "Blancas", "puntaje negro": negro, "puntaje blanco": blanco}
        else:
            return {"ganador": "Empate", "puntaje negro": negro, "puntaje blanco": blanco}



    #traduce el tablero que nos entrega el json y lo transforma al formato de 01-1-2 actualizando el tablero actual
    def traducir_tablero(self,tabla_de_actualizacion):
        for i in range(self.x):
            for j in range(self.y):
                if tabla_de_actualizacion['tablero'][i][j] == "cell empty":
                    self.tabla[i][j] = 0
                if tabla_de_actualizacion['tablero'][i][j] == "cell white":
                    self.tabla[i][j] = 2
                if tabla_de_actualizacion['tablero'][i][j] == "cell black":
                    self.tabla[i][j] = 1
                if tabla_de_actualizacion['tablero'][i][j] == "cell black attackable":
                    self.tabla[i][j] = -1
                if tabla_de_actualizacion['tablero'][i][j] == "cell white attackable":
                    self.tabla[i][j] = -2
                
    def cordenadas_posibles_jugadas(self, quien_juega):
        path = []
        for i in range(6):
            for j in range(6):
                self.actualiza_movimientos(quien_juega)
                if(self.tabla[i][j] == -(quien_juega)):
                    path.append([i,j])
        self.limpia_tablero()
        return path

    def cantidad_de_caminos(self, quien_juega):
        cantidad_de_movimientos = 0
        self.actualiza_movimientos(quien_juega)
        for i in range(self.x):
            for j in range(self.y):
                if(self.tabla[i][j] == -(quien_juega)):
                    cantidad_de_movimientos = cantidad_de_movimientos + 1
        return cantidad_de_movimientos
    #revisa si el juego a terminado
    def juego_terminado(self):
        for i in range(6):
            for j in range(6):
                self.actualiza_movimientos(1)
                if(self.tabla[i][j] == -1):
                    self.limpia_tablero()
                    return False
                self.limpia_tablero()
                self.actualiza_movimientos(2)
                if(self.tabla[i][j] == -2):
                    self.limpia_tablero()
                    return False
        return True

    #def calculo_de_flips(self,x1,y1, x2, y2):
    #    if(direccion == "arriba"):
    #        aux = 1 
    #        while (x1-aux != x2):
    #            self.tabla[x1-aux][y1] = num_evaluar
    #            aux = aux + 1 

    def revisa_si_existe_fichas_para_elegir(self, quien_juega):
        for i in range(self.x):
            for j in range(self.y):
                if(self.tabla[i][j] == -(quien_juega)):
                    return True

    def limpia_tablero(self):
        for i in range(self.x):
            for j in range(self.y):
                if(self.tabla[i][j] == -1 or self.tabla[i][j] == -2):
                    self.tabla[i][j] = 0 

    def actualiza_movimientos(self, quien_juega): 
        aux = 0
        for i in range(self.x):
            for j in range(self.y):

                if(self.tabla[i][j] == quien_juega):
                    self.movimiento_posible(i,j,quien_juega)
                    aux = aux + 1

        if aux == 0:
            return 0
        else:
            return 1
    
    def movimiento_posible(self ,cord_x, cord_y, num_evaluar):
        if(num_evaluar == 1):
            num_adversario = 2
        else:
            num_adversario = 1
        
        #preguntamos si existe un espacio a la arriba
        if(cord_x-1 >= 0):
            #preguntamos si el valor de arriba es una ficha adversaria
            if(self.tabla[cord_x-1][cord_y] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0):
                    if(self.tabla[cord_x-aux][cord_y] == 0):
                        self.tabla[cord_x-aux][cord_y] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x-aux][cord_y] == num_evaluar or self.tabla[cord_x-aux][cord_y] == -(num_evaluar)):
                        break
                    aux = aux + 1 


        #preguntamos si existe un espacio a la abajo
        if(cord_x+1 < 6):
            #preguntamos si abajo hay una ficha adversaria
            if(self.tabla[cord_x+1][cord_y] == num_adversario):
                aux = 2
                while (cord_x+aux < 6):
                    if(self.tabla[cord_x+aux][cord_y] == 0):
                        self.tabla[cord_x+aux][cord_y] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x+aux][cord_y] == num_evaluar or self.tabla[cord_x+aux][cord_y] == -(num_evaluar)):
                        break
                    aux = aux + 1 
                #print("abajo hay una ficha contraria")


        
        #preguntamos si existe un espacio a la izq
        if(cord_y-1 >= 0):
            #preguntamos si a la izquierda hay una ficha contraria""
            if(self.tabla[cord_x][cord_y-1] == num_adversario):
                aux = 2
                while (cord_y-aux >= 0):
                    if(self.tabla[cord_x][cord_y-aux] == 0):
                        self.tabla[cord_x][cord_y-aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x][cord_y-aux] == num_evaluar or self.tabla[cord_x][cord_y-aux] == -(num_evaluar)):
                        break
                    aux = aux + 1 
                #print("izquierda hay una ficha contraria")



        #preguntamos si existe un espacio a la derecha
        if(cord_y+1 < 6):
            #preguntamos si a la derecha hay una ficha contraria""
            if(self.tabla[cord_x][cord_y+1] == num_adversario):
                aux = 2
                while (cord_y+aux < 6):
                    if(self.tabla[cord_x][cord_y+aux] == 0):
                        self.tabla[cord_x][cord_y+aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x][cord_y+aux] == num_evaluar or self.tabla[cord_x][cord_y+aux] == -(num_evaluar)):
                        break
                    aux = aux + 1
                #print("derecha hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal inferior izquierda"
        if(cord_x-1 >= 0 and cord_y-1 >= 0):
            #preguntamos si hay una ficha contraria" arriba izq"
            if(self.tabla[cord_x-1][cord_y-1] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0 and cord_y-aux >= 0):
                    if(self.tabla[cord_x-aux][cord_y-aux] == 0):
                        self.tabla[cord_x-aux][cord_y-aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x-aux][cord_y-aux] == num_evaluar or self.tabla[cord_x-aux][cord_y-aux] == -(num_evaluar)):
                        break
                    aux = aux + 1
                #print("arriba izq hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal superior izquierda"
        if(cord_x-1 >= 0 and cord_y+1 < 6):
            #preguntamos si hay una ficha contraria" arriba derecha"
            if(self.tabla[cord_x-1][cord_y+1] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0 and cord_y+aux < 6):
                    if(self.tabla[cord_x-aux][cord_y+aux] == 0):
                        self.tabla[cord_x-aux][cord_y+aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x-aux][cord_y+aux] == num_evaluar or self.tabla[cord_x-aux][cord_y+aux] == -(num_evaluar)):
                        break
                    aux = aux + 1
                #print("arriba derecha hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal abajo derecha"
        if(cord_x+1 < 6 and cord_y+1 < 6):
            #preguntamos si hay una ficha contraria" abajo derecha"
            if(self.tabla[cord_x+1][cord_y+1] == num_adversario):
                aux = 2
                while (cord_x+aux < 6 and cord_y+aux < 6):
                    if(self.tabla[cord_x+aux][cord_y+aux] == 0):
                        self.tabla[cord_x+aux][cord_y+aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x+aux][cord_y+aux] == num_evaluar or self.tabla[cord_x+aux][cord_y+aux] == -(num_evaluar)):
                        break
                    aux = aux + 1
                #print("abajo derecha hay una ficha contraria")

                
        
        #verifica si existe camino hacia "diagonal abajo izq"
        if(cord_x+1 < 6 and cord_y-1 >= 0):
            #preguntamos si hay una ficha contraria" abajo izq"
            if(self.tabla[cord_x+1][cord_y-1] == num_adversario):
                aux = 2
                while (cord_x+aux < 6 and cord_y-aux >= 0):
                    if(self.tabla[cord_x+aux][cord_y-aux] == 0):
                        self.tabla[cord_x+aux][cord_y-aux] = -(num_evaluar)
                        break
                    if(self.tabla[cord_x+aux][cord_y-aux] == num_evaluar or self.tabla[cord_x+aux][cord_y-aux] == -(num_evaluar)):
                        break
                    aux = aux + 1
                #print("abajo izq hay una ficha contraria")

    def flip(self, x1,y1, x2, y2, num_evaluar, direccion):         
        if(direccion == "arriba"):
            aux = 1
            self.tabla[x1][y1] = num_evaluar 
            while (x1-aux != x2):
                self.tabla[x1-aux][y1] = num_evaluar
                aux = aux + 1 

        if(direccion == "abajo"):
            aux = 1
            self.tabla[x1][y1] = num_evaluar
            while (x1+aux != x2):
                self.tabla[x1+aux][y1] = num_evaluar
                aux = aux + 1

        if(direccion == "izquierda"):
            aux = 1  
            self.tabla[x1][y1] = num_evaluar   
            while (y1-aux != y2):
                self.tabla[x1][y1-aux] = num_evaluar
                aux = aux + 1

        if(direccion == "derecha"):
            aux = 1 
            self.tabla[x1][y1] = num_evaluar    
            while (y1+aux != y2):
                self.tabla[x1][y1+aux] = num_evaluar
                aux = aux + 1

        if(direccion == "arriba izquierda"):
            aux = 1  
            self.tabla[x1][y1] = num_evaluar   
            while (x1-aux != x2 and y1-aux != y2):
                self.tabla[x1-aux][y1-aux] = num_evaluar
                aux = aux + 1  

        if(direccion == "arriba derecha"):
            aux = 1  
            self.tabla[x1][y1] = num_evaluar   
            while (x1-aux != x2 and y1+aux != y2):
                self.tabla[x1-aux][y1+aux] = num_evaluar
                aux = aux + 1   

        if(direccion == "abajo derecha"):
            aux = 1    
            self.tabla[x1][y1] = num_evaluar 
            while (x1+aux != x2 and y1+aux != y2):
                self.tabla[x1+aux][y1+aux] = num_evaluar
                aux = aux + 1 

        if(direccion == "abajo izquierda"):
            aux = 1    
            self.tabla[x1][y1] = num_evaluar 
            while (x1+aux != x2 and y1-aux != y2):
                self.tabla[x1+aux][y1-aux] = num_evaluar
                aux = aux + 1

    def aplica_jugada(self,cord_x, cord_y, num_evaluar):
        if(num_evaluar == 1):
            num_adversario = 2
        else:
            num_adversario = 1
        #preguntamos si existe un espacio a la arriba
        if(cord_x-1 >= 0):
            #preguntamos si el valor de arriba es una ficha adversaria
            if(self.tabla[cord_x-1][cord_y] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0):
                    if(self.tabla[cord_x-aux][cord_y] == num_evaluar):
                        #aqui va funcion que recorre desde el punto x1,y1, hasta x2,y2 y los cambia aplica el flip
                        self.flip(cord_x,cord_y, cord_x-aux, cord_y, num_evaluar, "arriba")
                        break
                    aux = aux + 1 


        #preguntamos si existe un espacio a la abajo
        if(cord_x+1 < 6):
            #preguntamos si abajo hay una ficha adversaria
            if(self.tabla[cord_x+1][cord_y] == num_adversario):
                aux = 2
                while (cord_x+aux < 6):
                    if(self.tabla[cord_x+aux][cord_y] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x+aux, cord_y, num_evaluar, "abajo")
                        break
                    aux = aux + 1 


        
        #preguntamos si existe un espacio a la izq
        if(cord_y-1 >= 0):
            #preguntamos si a la izquierda hay una ficha contraria""
            if(self.tabla[cord_x][cord_y-1] == num_adversario):
                aux = 2
                while (cord_y-aux >= 0):
                    if(self.tabla[cord_x][cord_y-aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x, cord_y-aux, num_evaluar, "izquierda")    
                        break
                    aux = aux + 1 
                #print("izquierda hay una ficha contraria")



        #preguntamos si existe un espacio a la derecha
        if(cord_y+1 < 6):
            #preguntamos si a la derecha hay una ficha contraria""
            if(self.tabla[cord_x][cord_y+1] == num_adversario):
                aux = 2
                while (cord_y+aux < 6):
                    if(self.tabla[cord_x][cord_y+aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x, cord_y+aux, num_evaluar, "derecha")
                        break
                    aux = aux + 1
                #print("derecha hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal inferior izquierda"
        if(cord_x-1 >= 0 and cord_y-1 >= 0):
            #preguntamos si hay una ficha contraria" arriba izq"
            if(self.tabla[cord_x-1][cord_y-1] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0 and cord_y-aux >= 0):
                    if(self.tabla[cord_x-aux][cord_y-aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x-aux, cord_y, num_evaluar, "arriba izquierda")
                        break
                    aux = aux + 1
                #print("arriba izq hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal superior izquierda"
        if(cord_x-1 >= 0 and cord_y+1 < 6):
            #preguntamos si hay una ficha contraria" arriba derecha"
            if(self.tabla[cord_x-1][cord_y+1] == num_adversario):
                aux = 2
                while (cord_x-aux >= 0 and cord_y+aux < 6):
                    if(self.tabla[cord_x-aux][cord_y+aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x-aux, cord_y+aux, num_evaluar, "arriba derecha")
                        break
                    aux = aux + 1
                #print("arriba derecha hay una ficha contraria")


        
        #verifica si existe camino hacia "diagonal abajo derecha"
        if(cord_x+1 < 6 and cord_y+1 < 6):
            #preguntamos si hay una ficha contraria" abajo derecha"
            if(self.tabla[cord_x+1][cord_y+1] == num_adversario):
                aux = 2
                while (cord_x+aux < 6 and cord_y+aux < 6):
                    if(self.tabla[cord_x+aux][cord_y+aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x+aux, cord_y+aux, num_evaluar, "abajo derecha")
                        break
                    aux = aux + 1
                #print("abajo derecha hay una ficha contraria")

                
        
        #verifica si existe camino hacia "diagonal abajo izq"
        if(cord_x+1 < 6 and cord_y-1 >= 0):
            #preguntamos si hay una ficha contraria" abajo izq"
            if(self.tabla[cord_x+1][cord_y-1] == num_adversario):
                aux = 2
                while (cord_x+aux < 6 and cord_y-aux >= 0):
                    if(self.tabla[cord_x+aux][cord_y-aux] == num_evaluar):
                        self.flip(cord_x,cord_y, cord_x+aux, cord_y+aux, num_evaluar, "abajo izquierda")
                        break
                    aux = aux + 1
                #print("abajo izq hay una ficha contraria")