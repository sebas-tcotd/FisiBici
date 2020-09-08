'''
login.py: Modulo para el registro
'''
from datetime import datetime
from Backend.utils.utils import json_message
from Backend.models.user import User


class Register:
    '''
    Clase que registra a un usuario
    '''
    def __call__(self, request):

        email = request.json['email']

        user_obj = User.objects(
            email=email
        ).first()

        if user_obj is None:
            new_user = User(
                name=request.json['name'],
                last_name=request.json['last_name'],
                telephone=request.json['telephone'],
                birthdate=datetime(
                    request.json['birthdate']['year'],
                    request.json['birthdate']['month'],
                    request.json['birthdate']['day']
                ),
                password=request.json['password'],
                email=email,
                residence=request.json['residence'],
                district=request.json['district'],
                postal_code=request.json['postal_code']
            )

            new_user.save()
            return json_message("Usuario registrado")

        return json_message("Usuario ya registrado")
