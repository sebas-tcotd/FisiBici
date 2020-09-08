'''
config.py: modulo donde se configura la aplicación
'''
from flask import Flask
from flask_cors import CORS
from mongoengine import connect

def config_app(app):
    app.secret_key = 'clavesecreta'

    DB_URI = "mongodb+srv://Mauricio:1234@fisibici"
    DB_URI += ".cpmx7.mongodb.net/SistemaBicicletas?retryWrites=true&w=majority"
    connect(host=DB_URI)

    CORS(app=app, supports_credentials=True)

def config_app_production(app):
    config_app(app)

    app.config.update(
        SERVER_NAME='fisi-bici.herokuapp.com',
        SESSION_COOKIE_NAME='fisi-bici.herokuapp.com',
        SESSION_COOKIE_DOMAIN='fisi-bici.herokuapp.com',
    )

def config_app_development(app):
    config_app(app)

    app.config.update(
        SERVER_NAME='127.0.0.1:5000',
        SESSION_COOKIE_NAME='127.0.0.1:5000',
        SESSION_COOKIE_DOMAIN='127.0.0.1:5000',
    )
