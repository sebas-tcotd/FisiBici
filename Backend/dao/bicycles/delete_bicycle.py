from flask import jsonify
from models.bicycle import Bicycle

class DeleteBicycle:

    def __call__(self,bicycle_name):

        bicycle_obj = Bicycle.objects(
            name=bicycle_name
        ).first()

        if bicycle_obj is not None:
            bicycle_obj.delete()

            return jsonify({
                "message": "bicycle deleted",
            })

        return jsonify({
            "message": "bicycle not found"
        })