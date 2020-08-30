from flask import jsonify
from models.bicycle import Bicycle

class UpdateBicycle:

    def __call__(self,request,bicycle_id):

        bicycle_obj = Bicycle.objects(
            id=bicycle_id
        ).first()

        if bicycle_obj is not None:
            if "name" in request.json:
                bicycle_obj.name = request.json["name"]
            if "price" in request.json:
                bicycle_obj.price = request.json["price"]
            if "stock" in request.json:
                bicycle_obj.stock = request.json["stock"]
            if "colors" in request.json:
                bicycle_obj.colors = request.json["colors"]
            if "use" in request.json:
                bicycle_obj.use = request.json["use"]
            bicycle_obj.save()

            return jsonify({
                "message": "bicycle updated",
                "bicycle": bicycle_obj.json()
            })

        return jsonify({
            "message": "bicycle not found"
        })