from flask import Blueprint

#Crear y configurar mi blueprint 
mi_blueprint = Blueprint('mi_blueprint', 
                         __name__,
                         url_prefix = '/ejemplo' )

#Crear ruta del blueprint
@mi_blueprint.route('/saludo')
def saludo():
    return 'hay otros generos'
