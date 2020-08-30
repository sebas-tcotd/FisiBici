from flask import jsonify
from models.bicycle import Bicycle

class StoreBicycle:

    def __call__(self,request):
        new_bicycle = Bicycle(
            name=request.json["name"],
            price=request.json["price"],
            colors=request.json["colors"]
        )

        if "stock" in request.json:
            new_bicycle.stock = request.json["stock"]
        if "use" in request.json:
            new_bicycle.stock = request.json["use"]

        new_bicycle.save()
        return jsonify({
            "message": "bicycle added succesfully",
            "bicycle": new_bicycle.json()
        })