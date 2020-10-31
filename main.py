from flask import Flask , render_template, request
from Tablero import Tablero
#from ia import ia


app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def home():
    content = request.get_json(silent=True)
    print("contac",content)

    juego_nuevo = gameplay()

    print("tablero",juego_nuevo.tabla)
    return render_template('home.html', tabla=juego_nuevo.tabla)


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
    
    return juego_nuevo
 