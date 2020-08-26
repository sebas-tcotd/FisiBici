from flask import jsonify
from models.bicycle import Bicycle

class GetBicycle:

    def __call__(self,bicycle_name):

        bicycle_obj = Bicycle.objects(
            name=bicycle_name
        ).first()

        if (bicycle_obj is not None):
            return jsonify({"bicycle": bicycle_obj.json()})

        return jsonify({"message": "bicycle not found" })