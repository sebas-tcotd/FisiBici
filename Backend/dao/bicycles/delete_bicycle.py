'''
delete_bicycles.py: Modulo para borrar una bicicleta
'''
from flask import jsonify
from Backend.models.bicycle import Bicycle


class DeleteBicycle:
    '''
    Clase que borra una bicicleta
    '''
    def __call__(self, bicycle_id):

        bicycle_obj = Bicycle.objects(
            id=bicycle_id
        ).first()

        if bicycle_obj is not None:
            bicycle_obj.delete()

            return jsonify({
                "message": "bicycle deleted",
            })

        return jsonify({
            "message": "bicycle not found"
        })
