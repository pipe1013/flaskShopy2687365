from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NewProductForm(FlaskForm):
    productname = StringField("Nombre producto:")
    precio = StringField("Precio producto:")
    submit = SubmitField("Registrar Producto")
    