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


    @app.route('/auth/register')
    def register():
        return render_template('singup.html')
