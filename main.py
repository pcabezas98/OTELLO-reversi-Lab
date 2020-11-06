from flask import Flask , render_template, request, jsonify
from Tablero import Tablero
from ia import *
import copy
from time import time



app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def inicio():
     
    return render_template('home.html')



@app.route('/game')
def home():
     
    return render_template('juego.html')


@app.route('/receiver', methods = ['POST'])
def worker():
    data = request.get_json(silent=True)
    juego_nuevo = Tablero()
    juego_nuevo.traducir_tablero(data)

    if data['espero'] == 'ayuda':
        nivel = definir_nivel(data)
        if(nivel == 'Error'):
            return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="ERROR EN LA ENTRADA")

        pos = minimax(juego_nuevo, 1 ,1, 2, nivel)
        print(f"\nmejor valor: {pos[0]}, con cordenada {pos[1]}")
  

        return jsonify(mov_ayuda=pos[1])


    #mandar tablero posible jugada humano
    if data['espero'] == 'inicio_juego':
        juego_nuevo.actualiza_movimientos(1)


        #creamos partida contra humano vs humano
        if data['ficha jugada'] == 'HUMAN':
            return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 1")


        #creamos partida contra humano vs IA
        if data['ficha jugada'] == 'IA':
            nivel = definir_nivel(data)
            if(nivel == 'Error'):
                return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="ERROR EN LA ENTRADA")

            return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="Te toca")
            


    if data['turno jugador'] == 'Turno Maquina':
        juego_nuevo.limpia_tablero()

        if juego_nuevo.cantidad_de_caminos(1) == 0 and juego_nuevo.cantidad_de_caminos(2) == 0:
            resultados = juego_nuevo.ganador()
            if resultados['ganador'] == 'blanca':
                ganador_ia = "Perdiste"
            else:
                ganador_ia = "Ganaste"
            return jsonify(tablero_espera=juego_nuevo.tabla,
                                    turno="El juego ha terminado", ganador=ganador_ia,
                                    puntaje_blanco=resultados['puntaje blanco'],
                                    puntaje_negro=resultados['puntaje negro'])

        if juego_nuevo.cantidad_de_caminos(2) == 0:
            juego_nuevo.actualiza_movimientos(1)
            return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="Te toca")

        nivel = definir_nivel(data)
        if(nivel == 'Error'):
            return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="ERROR EN LA ENTRADA")

        juego_nuevo.limpia_tablero()
        juego_nuevo.actualiza_movimientos(2)
        #si existe jugada entra al if por que aun quedan jugadas, sino el juego ha terminado
        if juego_nuevo.revisa_si_existe_fichas_para_elegir(2):
            juego_nuevo.limpia_tablero()
            #se empieza a tomar el timepo
            comienzo_t = time()
            pos = minimax(juego_nuevo, 2 ,2, 1, nivel)
            #se termina de tomar el tiempo
            timepo_total = time() - comienzo_t
            print(f"\nmejor valor: {pos[0]}, con cordenada {pos[1]}")
            print(f"tiempo de respuesta minimax: {timepo_total}")

            #se crea el tablero con el movimiento aplicado
            juego_nuevo.aplica_jugada(pos[1][0],pos[1][1],2)
            
            if juego_nuevo.cantidad_de_caminos(1) == 0:
                resultados = juego_nuevo.ganador()
                if resultados['ganador'] == 'blanca':
                    ganador_ia = "Perdiste"
                else:
                    ganador_ia = "Ganaste"
                return jsonify(tablero_espera=juego_nuevo.tabla,
                                    turno="El juego ha terminado", ganador=ganador_ia,
                                    puntaje_blanco=resultados['puntaje blanco'],
                                    puntaje_negro=resultados['puntaje negro'])
            
            juego_nuevo.limpia_tablero()
            juego_nuevo.actualiza_movimientos(1)
            return jsonify(tablero_espera=juego_nuevo.tabla,
                            turno="Te toca")



             
    #mandar 3 tableros, posible jugada ia (time 2sec.), jugada ia, posible jugada humao
    if  data['turno jugador'] == 'Te toca':
        juego_nuevo.limpia_tablero()
        juego_nuevo.actualiza_movimientos(1)
        #si existe jugada entra al if por que aun quedan jugadas, sino el juego ha terminado
        if juego_nuevo.revisa_si_existe_fichas_para_elegir(1):
            juego_nuevo.limpia_tablero()
            ficha_jugada = data['ficha jugada']
            juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),1)
            juego_nuevo.limpia_tablero()

            return jsonify(tablero_espera=juego_nuevo.tabla,
                        turno="Turno Maquina")
        juego_nuevo.limpia_tablero()

        if juego_nuevo.cantidad_de_caminos(1) == 0 and juego_nuevo.cantidad_de_caminos(2) == 0:
            resultados = juego_nuevo.ganador()
            if resultados['ganador'] == 'blanca':
                ganador_ia = "Perdiste"
            else:
                ganador_ia = "Ganaste"
            return jsonify(tablero_espera=juego_nuevo.tabla,
                                    turno="El juego ha terminado", ganador=ganador_ia,
                                    puntaje_blanco=resultados['puntaje blanco'],
                                    puntaje_negro=resultados['puntaje negro'])

        juego_nuevo.limpia_tablero()
        return jsonify(tablero_espera=juego_nuevo.tabla,
                        turno="Turno Maquina")
       



    if  data["turno jugador"] == "Jugador 1" or data["turno jugador"] == "Jugador 2":
        ficha_jugada = data['ficha jugada']
        #ACTUALIZAMOS EL TABLERO PERO ANTES LIMPIAMOS LOS -1 O -2
        if data["turno jugador"] == "Jugador 1":
            juego_nuevo.limpia_tablero()
            juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),1)
            juego_nuevo.actualiza_movimientos(2)
            if juego_nuevo.revisa_si_existe_fichas_para_elegir(2):
                return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 2")
            else:
                juego_nuevo.actualiza_movimientos(1)
                if juego_nuevo.revisa_si_existe_fichas_para_elegir(1):
                    return jsonify(tablero_espera=juego_nuevo.tabla,
                        turno="Jugador 1", mensaje="El jugador 2 se quedo sin movimientos")

                resultados = juego_nuevo.ganador()

                return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="El juego ha terminado", ganador=resultados['ganador'],
                                puntaje_blanco=resultados['puntaje blanco'],
                                puntaje_negro=resultados['puntaje negro'])    
            
        
        if data["turno jugador"] == "Jugador 2":
            juego_nuevo.limpia_tablero()
            juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),2)
            juego_nuevo.actualiza_movimientos(1)
            if juego_nuevo.revisa_si_existe_fichas_para_elegir(1):
                return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 1")
            
            else:
                juego_nuevo.actualiza_movimientos(2) 
                if juego_nuevo.revisa_si_existe_fichas_para_elegir(2):
                    juego_nuevo.actualiza_movimientos(2)
                    return jsonify(tablero_espera=juego_nuevo.tabla,
                        turno="Jugador 2", mensaje="El jugador 1 se quedo sin movimientos")
                
                resultados = juego_nuevo.ganador()

                return jsonify(tablero_espera=juego_nuevo.tabla,
                                turno="El juego ha terminado", ganador=resultados['ganador'],
                                puntaje_blanco=resultados['puntaje blanco'],
                                puntaje_negro=resultados['puntaje negro']) 

       
    


    return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="ERROR")

app.run(Host='0.0.0.0')


def definir_nivel(data):
    if(data['dificultad'] == 'Facil' or data['dificultad'] == 'Nivel: Facil'):
        dificultad = 1
        return dificultad
    elif (data['dificultad'] == 'Medio' or data['dificultad'] == 'Nivel: Medio'):
        dificultad = 3
        return dificultad
    elif (data['dificultad'] == 'Dificil' or data['dificultad'] == 'Nivel: Dificil'):
        dificultad = 5
        return dificultad
    else:
        return "Error"

