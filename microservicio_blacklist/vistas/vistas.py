import datetime
import json
from flask_restful import Resource
from ..modelos import db, Black, User, BlackSchema, UserSchema
from flask import make_response, request, session

black_schema = BlackSchema()

class VistaBlacks(Resource):

    def get(self):
               
        return [black_schema.dump(black) for black in Black.query.all()]
    
    def post(self):
        nuevo_black = Black(email=request.json['email'],id_app_cliente=request.json['id_app_cliente'],motivo=request.json['motivo'] )
        #falta  lo de guardar la ip
        db.session.add(nuevo_black)
        db.session.commit()
        #resp = make_response(json.dumps(nuevo_black), "El correo fue agregado exitosamente a la lista")     
        return black_schema.dump(nuevo_black)

class VistaBlack(Resource):

    def get(self, email):
        
        black_customer = Black.query.filter_by(email = email).first()
        return black_schema.dump(black_customer)