'''
config.py: modulo donde se configura la aplicación
'''


def config_app(app):
    app.secret_key = 'clavesecreta'

    app.config.update(
        SERVER_NAME='fisi-bici.herokuapp.com',
        SESSION_COOKIE_NAME='fisi-bici.herokuapp.com',
        SESSION_COOKIE_DOMAIN='fisi-bici.herokuapp.com',
    )
