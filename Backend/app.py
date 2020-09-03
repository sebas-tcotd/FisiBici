'''Archivo que ejecuta la aplicacion'''
from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from config.config import config_app
from routes.bicycles import create_routes_bicycles
from routes.login import create_routes_login

app = Flask(__name__)
connect("SistemaBicicletas")
CORS(app, resources={r"/*": {"origins": "*"}})

config_app(app)
create_routes_bicycles(app)
create_routes_login(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
