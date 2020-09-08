'''Archivo que ejecuta la aplicacion'''
from flask import Flask, render_template

from config.config import config_app_production
from routes.views import create_routes_views
from routes.bicycles import create_routes_bicycles
from routes.login import create_routes_login

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')

config_app_production(app)
create_routes_views(app)
create_routes_bicycles(app)
create_routes_login(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
