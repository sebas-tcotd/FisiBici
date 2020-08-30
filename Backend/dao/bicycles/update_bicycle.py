from flask import jsonify
from models.bicycle import Bicycle

class UpdateBicycle:

    def __call__(self,request,bicycle_name):

        bicycle_obj = Bicycle.objects(
            name=bicycle_name
        ).first()

        if bicycle_obj is not None:
            bicycle_obj.name = request.json["name"]
            bicycle_obj.price = request.json["price"]
            bicycle_obj.save()

            return jsonify({
                "message": "bicycle updated",
                "bicycle": bicycle_obj.json()
            })

        return jsonify({
            "message": "bicycle not found"
        })