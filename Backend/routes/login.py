'''
login.py: Modulo para definir las rutas relacionadas con la API login
'''
from flask import request
from dao.login.login import Login
from dao.login.register import Register
from dao.login.get_current_user import GetCurrentUser
from dao.login.sign_off import SignOff

def create_routes_login(app):
    '''
    Metodo que crea las rutas relacionadas con la API login
    '''
    #pylint: disable=unused-variable
    @app.route('/register', methods=['POST'])
    def register():
        register = Register()
        return register(request)

    #pylint: disable=unused-variable
    @app.route('/login', methods=['POST'])
    def login():
        login = Login()
        return login(request)

    #pylint: disable=unused-variable
    @app.route('/user')
    def get_current_user():
        current_user = GetCurrentUser()
        return current_user()

    #pylint: disable=unused-variable
    @app.route('/user', methods=['DELETE'])
    def sign_off():
        sign_off = SignOff()
        return sign_off()
