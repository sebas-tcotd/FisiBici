'''Archivo que ejecuta la aplicacion'''
from flask import Flask, session
from mongoengine import connect
from routes.bicycles import create_routes_bicycles
from routes.login import create_routes_login

app = Flask(__name__)
connect("SistemaBicicletas")
app.secret_key = 'clavesecreta'

create_routes_bicycles(app)
create_routes_login(app)

app.config.update(
    SERVER_NAME = '127.0.0.1:5000',
    SESSION_COOKIE_DOMAIN = '127.0.0.1:5000'
)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
