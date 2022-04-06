from datetime import datetime
import json
from flask_restful import Resource
from ..modelos import db, Black, User, BlackSchema, UserSchema
from flask import make_response, request, session
#from flask_jwt_extended import jwt_required, create_access_token

black_schema = BlackSchema()

class VistaBlacks(Resource):

    def get(self):
               
        return [black_schema.dump(black) for black in Black.query.all()]
    
    def post(self):
        print('ip', request.remote_addr)
        nuevo_black = Black(email=request.json['email'],id_app_cliente=request.json['id_app_cliente'],motivo=request.json['motivo'], ip=request.remote_addr, fecha=datetime.now())
        #falta  lo de guardar la ip
        db.session.add(nuevo_black)
        db.session.commit()
        validacion = Black.query.filter_by(email=request.json['email'], id_app_cliente = request.json['id_app_cliente']).all()
        if validacion:
                return {'mensaje':'El email fue exitosamente añadido a la lista negra'}, 200
        else:
                return {'mensaje':'Error al añadir el email a la lista negra'}, 401

class VistaBlack(Resource):

    def get(self, email):
        
        black_customer = Black.query.filter_by(email = email).first()
        if black_customer:
            return black_schema.dump(black_customer)
        else:
            return {'mensaje':'El email no se encuentra en la lista negra'}, 404