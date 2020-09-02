from flask import session
from utils.utils import json_message

class SignOff:

    def __call__(self):

        if "user_id" in session:
            if session['user_id'] is not None:
                session['user_id'] = None

                return json_message("Sesion cerrada")

            return json_message("Ningun usuario ha iniciado sesion")

        return json_message("Ningun usuario ha iniciado sesion")