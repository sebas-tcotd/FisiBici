'''Archivo que ejecuta la aplicacion'''
from flask import Flask
from mongoengine import connect
from routes.bicycles import create_routes_bicycles
from routes.login import create_routes_login

app = Flask(__name__)
connect("SistemaBicicletas")
app.secret_key = 'clavesecreta'

create_routes_bicycles(app)
create_routes_login(app)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
