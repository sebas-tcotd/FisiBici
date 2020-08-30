from flask import jsonify
from models.bicycle import Bicycle

class GetBicycle:

    def __call__(self,bicycle_id):

        bicycle_obj = Bicycle.objects(
            id=bicycle_id
        ).first()

        if (bicycle_obj is not None):
            return jsonify({"bicycle": bicycle_obj.json()})

        return jsonify({"message": "bicycle not found" })