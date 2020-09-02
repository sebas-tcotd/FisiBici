from utils.utils import json_message
from models.user import User

class Register:

    def __call__(self,request):

        email = request.json['email']

        user_obj = User.objects(
            email=email
        ).first()

        if user_obj is None:

            new_user = User(
                password=request.json['password'],
                email=email,
                residence=request.json['residence'],
                district=request.json['district'],
                postal_code=request.json['postal_code']
            )

            new_user.save()
            return json_message("Usuario registrado")

        return json_message("Usuario ya registrado")