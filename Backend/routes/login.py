from flask import request
from dao.login.login import Login
from dao.login.register import Register
from dao.login.get_current_user import GetCurrentUser
from dao.login.sign_off import SignOff

def create_routes_login(app):
    @app.route('/register', methods=['POST'])
    def register():
        register = Register()
        return register(request)

    @app.route('/login', methods=['POST'])
    def login():
        login = Login()
        return login(request)

    @app.route('/user')
    def get_current_user():
        current_user = GetCurrentUser()
        return current_user()

    @app.route('/user', methods=['DELETE'])
    def signOff():
        signOff = SignOff()
        return signOff()