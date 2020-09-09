'''
views.py: Modulo para definir las rutas relacionadas con las vistas
'''
from flask import render_template

def create_routes_views(app):
    '''
    Metodo que crea las rutas relacionadas con las vistas
    '''
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/auth/sign-up')
    def sign_up():
        return render_template('signup.html')

    @app.route('/auth/sign-in')
    def sign_in():
        return render_template('singin.html')

    @app.route('/shop')
    def shop():
        return render_template('shop.html')
