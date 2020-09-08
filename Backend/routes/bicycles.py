'''
bicycles.py: Modulo para definir las rutas relacionadas con la API bicicletas
'''
from flask import request

from Backend.dao.bicycles.store_bicycle import StoreBicycle
from Backend.dao.bicycles.get_bicycles import GetBicycles
from Backend.dao.bicycles.get_bicycle import GetBicycle
from Backend.dao.bicycles.update_bicycle import UpdateBicycle
from Backend.dao.bicycles.delete_bicycle import DeleteBicycle


def create_routes_bicycles(app):
    '''
    Metodo que crea las rutas relacionadas con la API bicicletas
    '''
    # pylint: disable=unused-variable
    @app.route('/bicycles')
    def get_bicycles():
        get_bicycles = GetBicycles()
        return get_bicycles()

    # pylint: disable=unused-variable
    @app.route('/bicycles/<string:bicycle_id>')
    def get_bicycle(bicycle_id):
        get_bicycle = GetBicycle()
        return get_bicycle(bicycle_id)

    # pylint: disable=unused-variable
    @app.route('/bicycles', methods=['POST'])
    def add_bicycle():
        store_bicycle = StoreBicycle()
        return store_bicycle(request)

    # pylint: disable=unused-variable
    @app.route('/bicycles/<string:bicycle_id>', methods=['PUT'])
    def update_bicycle(bicycle_id):
        update_bicycle = UpdateBicycle()
        return update_bicycle(request, bicycle_id)

    # pylint: disable=unused-variable
    @app.route('/bicycles/<string:bicycle_id>', methods=['DELETE'])
    def delete_bicycle(bicycle_id):
        delete_bicycle = DeleteBicycle()
        return delete_bicycle(bicycle_id)
