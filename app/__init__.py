from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .mi_blueprint import mi_blueprint
from flask_bootstrap import Bootstrap

#Blueprints
from .mi_blueprint import mi_blueprint
from app.productos import productos

#Creacion y configuracion de la app
app = Flask(__name__)
app.config.from_object(Config)
boostrap = Bootstrap(app)

#Registro de blueprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#CREAR LOS OBJETOS DE SQLALCHEMY Y MIGRATE 
db = SQLAlchemy(app)
migrate = Migrate(app , 
                  db)

from .models import Producto, Cliente, Venta, Detalle
