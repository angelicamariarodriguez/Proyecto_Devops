from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proyecto:proyecto@aa1dwcgg1jsrmhk.c6bctyrz9gs4.us-east-1.rds.amazonaws.com/ebdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    return app