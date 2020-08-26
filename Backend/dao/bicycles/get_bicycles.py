from flask import jsonify
from models.bicycle import Bicycle

class GetBicycles:

    def __call__(self):
        bicycles_objs = Bicycle.objects()
        bicycles = []

        for bicycle in bicycles_objs:
            bicycles.append(bicycle.json())

        return jsonify({"bicycles": bicycles, "message": "bicycles's List"})