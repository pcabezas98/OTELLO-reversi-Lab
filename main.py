from flask import Flask , render_template, request, jsonify
from Tablero import Tablero
from ia import *



app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
     
    return render_template('home.html')


@app.route('/receiver', methods = ['POST'])
def worker():
    data = request.get_json(silent=True)
    juego_nuevo = Tablero()
    juego_nuevo.traducir_tablero(data)

    #mandar tablero posible jugada humano
    if data['espero'] == 'inicio_juego':
        juego_nuevo.actualiza_movimientos(1)
        #creamos partida contra humano vs humano
        if data['ficha jugada'] == 'HUMAN':
            return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 1")
        #creamos partida contra humano vs IA
        if data['ficha jugada'] == 'IA':
            return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Te toca")
            

    #mandar 3 tableros, posible jugada ia (time 2sec.), jugada ia, posible jugada humao
    if data['espero'] == 'jugada ia':
        ficha_jugada = data['ficha jugada']
        #ACTUALIZAMOS EL TABLERO PERO ANTES LIMPIAMOS LOS -1 O -2
        juego_nuevo.limpia_tablero()
        juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),1)
        pass
    #print(data['ficha jugada'])

    if data['espero'] == 'jugada humano' or data["turno jugador"] == "Jugador 1" or data["turno jugador"] == "Jugador 2":
        ficha_jugada = data['ficha jugada']
        #ACTUALIZAMOS EL TABLERO PERO ANTES LIMPIAMOS LOS -1 O -2
        print(data["turno jugador"])
        if data["turno jugador"] == "Jugador 1":
            juego_nuevo.limpia_tablero()
            juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),1)
            juego_nuevo.actualiza_movimientos(2)
            return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 2")
        
        if data["turno jugador"] == "Jugador 2":
            juego_nuevo.limpia_tablero()
            juego_nuevo.aplica_jugada(int(ficha_jugada[1]),int(ficha_jugada[2]),2)
            juego_nuevo.actualiza_movimientos(1)
            return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="Jugador 1")

        pass
    
    
    #for i in juego_nuevo.tabla:
    #    print(i)

    return jsonify(tablero_espera=juego_nuevo.tabla,
                    turno="klfasdh")

app.run(Host='0.0.0.0')

def gameplay():
    
    juego_nuevo = Tablero()
    #for i in juego_nuevo.tabla:
    #    print(i)


    print("")
    juego_nuevo.aplica_jugada(2,1,1)
    juego_nuevo.actualiza_movimientos(1)
    #for i in juego_nuevo.tabla:
    #    print(i)

    return juego_nuevo
 