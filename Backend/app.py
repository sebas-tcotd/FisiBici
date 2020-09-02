from flask import Flask
from mongoengine import *

app = Flask(__name__)
connect("SistemaBicicletas")
app.secret_key = 'clavesecreta'

from routes.bicycles import create_routes_bicycles
from routes.login import create_routes_login

create_routes_bicycles(app)
create_routes_login(app)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
