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

    @app.route('/auth/singup')
    def singup():
        return render_template('singup.html')

    @app.route('/auth/singin')
    def singin():
        return render_template('singin.html')

    @app.route('/shop')
    def shop():
        return render_template('shop.html')
