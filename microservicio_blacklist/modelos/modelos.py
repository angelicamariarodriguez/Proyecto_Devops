from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

#blacks_users = db.Table('black_user', 
       # db.Column('black_id', db.Integer, db.ForeignKey('black.id'), primary_key=True),
       # db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True) )

class Black(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    id_app_cliente = db.Column(db.String(128))
    motivo = db.Column(db.String(255))
    ip = db.Column(db.String(128))
    fecha = db.Column(db.Date)
    #users = db.relationship('User', secondary='black_user', back_populates = 'blacks')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #blacks = db.relationship('Black', secondary='black_user', back_populates = 'users')


class BlackSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Black
        include_relationships = True
        load_instance = True 

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True 