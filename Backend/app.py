'''Archivo que ejecuta la aplicacion'''
from flask import Flask, render_template
from flask_cors import CORS
from mongoengine import connect

from Backend.config.config import config_app
from Backend.routes.bicycles import create_routes_bicycles
from Backend.routes.login import create_routes_login

static_path = '/../Frontend/static'

app = Flask(__name__, template_folder='../Frontend/templates', static_url_path=static_path)

app.static_url_path = static_path

for rule in app.url_map.iter_rules('static'):
    app.url_map._rules.remove(rule)

app.url_map._rules_by_endpoint['static'] = []

app.add_url_rule(f'{static_path}/<path:filename>',
                 endpoint='static',
                 view_func=app.send_static_file)

DB_URI = "mongodb+srv://Mauricio:1234@fisibici"
DB_URI += ".cpmx7.mongodb.net/SistemaBicicletas?retryWrites=true&w=majority"
connect(host=DB_URI)

@app.route('/')
def index():
    return render_template('index.html')

CORS(app=app, supports_credentials=True)

config_app(app)
create_routes_bicycles(app)
create_routes_login(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
