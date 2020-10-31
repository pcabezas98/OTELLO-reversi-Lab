from flask import Flask , render_template
from Tablero import Tablero
#from ia import ia


app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():

    gameplay()
    return render_template('home.html')


app.run(Host='0.0.0.0')



def gameplay():

    juego_nuevo = Tablero()
    for i in juego_nuevo.tabla:
        print(i)

    print("")
    juego_nuevo.actualiza_movimientos(1)

    for i in juego_nuevo.tabla:
        print(i)
 
    print("")
    juego_nuevo.limpia_tablero()
    juego_nuevo.aplica_jugada(2,1,1)

    for i in juego_nuevo.tabla:
        print(i)
 

    print("")
    juego_nuevo.aplica_jugada(1,3,2)
    for i in juego_nuevo.tabla:
        print(i)

    print("")
 

    juego_nuevo.actualiza_movimientos(1)

    for i in juego_nuevo.tabla:
        print(i)
 