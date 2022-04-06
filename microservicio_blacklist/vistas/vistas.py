from datetime import datetime
import json
from flask_restful import Resource
from ..modelos import db, Black, User, BlackSchema, UserSchema
from flask import make_response, request, session
#from flask_jwt_extended import jwt_required, create_access_token

black_schema = BlackSchema()

class VistaBlacks(Resource):

    TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    def get(self):
               
        return [black_schema.dump(black) for black in Black.query.all()]
    
    def post(self):

        header = request.headers
        bearer = header.get('Authorization')
        #token = bearer.split()[1] 
        print('el token es', bearer)

        if bearer== self.TOKEN:
            nuevo_black = Black(email=request.json['email'],id_app_cliente=request.json['id_app_cliente'],motivo=request.json['motivo'], ip=request.remote_addr, fecha=datetime.now())
            db.session.add(nuevo_black)
            db.session.commit()
            validacion = Black.query.filter_by(email=request.json['email'], id_app_cliente = request.json['id_app_cliente']).all()
            if validacion:
                    return {'mensaje':'El email fue exitosamente añadido a la lista negra'}, 200
            else:
                    return {'mensaje':'Error al añadir el email a la lista negra'}, 401
        else:
            return {'mensaje':'Usuario no autorizado'}, 500

class VistaBlack(Resource):

    def get(self, email):
        
        black_customer = Black.query.filter_by(email = email).first()
        if black_customer:
            return black_schema.dump(black_customer)
        else:
            return {'mensaje':'El email no se encuentra en la lista negra'}, 404