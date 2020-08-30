from flask import Flask, jsonify, request
from mongoengine import *

from dao.bicycles.store_bicycle import StoreBicycle
from dao.bicycles.get_bicycles import GetBicycles
from dao.bicycles.get_bicycle import GetBicycle
from dao.bicycles.update_bicycle import UpdateBicycle
from dao.bicycles.delete_bicycle import DeleteBicycle

#from dao.login.login import Login
#from dao.register.register import Register

app = Flask(__name__)
connect("SistemaBicicletas")
#app.secret_key = 'clavesecreta'

#bicycles
@app.route('/bicycles')
def get_bicycles():
    get_bicycles = GetBicycles()
    return get_bicycles()

@app.route('/bicycles/<string:bicycle_id>')
def get_bicycle(bicycle_id):
    get_bicycle = GetBicycle()
    return get_bicycle(bicycle_id)

@app.route('/bicycles', methods=['POST'])
def add_bicycle():
    store_bicycle = StoreBicycle()
    return store_bicycle(request)

@app.route('/bicycles/<string:bicycle_id>', methods=['PUT'])
def update_bicycle(bicycle_id):
    update_bicycle = UpdateBicycle()
    return update_bicycle(request,bicycle_id)

@app.route('/bicycles/<string:bicycle_id>', methods=['DELETE'])
def delete_bicycle(bicycle_id):
    delete_bicycle = DeleteBicycle()
    return delete_bicycle(bicycle_id)

#Registro
'''
@app.route('/register', methods=['POST'])
def register():
    register = Register()
    return register(request)

#Login
@app.route('/login', methods=['POST'])
def login():
    login = Login()
    return login(request)
'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
