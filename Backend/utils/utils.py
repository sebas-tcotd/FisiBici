'''
utils.py: Modulo para definir los metodos de funcionalidad auxiliar
'''
from flask import jsonify

def json_message(msg):
    '''
    Metodo que devuelve un mensaje en formato json
    '''
    return jsonify({
        "message": msg
    })
