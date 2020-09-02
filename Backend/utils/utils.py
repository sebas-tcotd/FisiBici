from flask import jsonify

def json_message(msg):
    return jsonify({
        "message": msg
    })