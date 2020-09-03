'''
login.py: Modulo para iniciar sesion
'''
from flask import session
from utils.utils import json_message
from models.user import User


class Login:
    '''
    Clase que inicia sesion
    '''
    def __call__(self, request):
        session.pop('user_id', None)
        request.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500500293,93874'

        user_email = request.json['email']
        password = request.json['password']

        user_obj = User.objects(
            email=user_email
        ).first()

        if user_obj is not None:
            if user_obj.password == password:
                session['user_id'] = user_obj.json()["user_id"]
                return json_message("Sesion Iniciada")

            return json_message("Contraseña incorrecta")

        return json_message("El usuario no está registrado")
