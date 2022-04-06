from microservicio_blacklist import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from .modelos import db, Black, User, BlackSchema, UserSchema
from .vistas import VistaBlack, VistaBlacks
#from flask_jwt_extended import JWTManager
import requests


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaBlacks, '/blacklists')
api.add_resource(VistaBlack, '/blacklists/<string:email>')

#jwt = JWTManager(app)