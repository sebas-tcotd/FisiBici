'''
get_bicycles.py: Modulo para obtener todas las bicicletas
'''
from flask import jsonify
from models.bicycle import Bicycle


class GetBicycles:
    '''
    Clase que obtiene todas las bicicletas
    '''
    def __call__(self):
        bicycles_objs = Bicycle.objects()
        bicycles = []

        for bicycle in bicycles_objs:
            bicycles.append(bicycle.json())

        return jsonify({"bicycles": bicycles, "message": "bicycles's List"})
