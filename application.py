from email.mime import application
from flask_restful import Resource, Api
from flask import Flask
from modelos.modelos import db
from vistas.vistas import VistaBlack, VistaBlacks


# APP config
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proyecto:proyecto@aa1dwcgg1jsrmhk.c6bctyrz9gs4.us-east-1.rds.amazonaws.com/ebdb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_context = application.app_context()
app_context.push()
db.init_app(application)
db.create_all()

api = Api(application)
api.add_resource(VistaBlacks, '/blacklists')
api.add_resource(VistaBlack, '/blacklists/<string:email>')


# Punto de arranque: gunicorn
def gunicorn():
    # Retornar el objeto de la aplicacion
    return application

# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    application.run(port = 5000, debug = True)
