from django.apps import AppConfig
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['operario-1']
    password = request.form['operario2024']
    
    # Aquí puedes manejar la lógica de inicio de sesión y asignación de usuario
    
    return "Inicio de sesión exitoso para el usuario: {}".format(username)

@app.route('/')
def index():
    return render_template('superA.html')

@app.route('/usuarios')
def crear_usuarios():
    return render_template('usuarios.html')

@app.route('/manejoProyecto')
def manejo_proyecto():
    return render_template('manejoProyecto.html')

if __name__ == '__main__':
    app.run(debug=True)

class CablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Cables'

from flask import Flask, request

app = Flask(__name__)


