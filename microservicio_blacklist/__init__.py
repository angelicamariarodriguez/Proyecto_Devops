from email.mime import application
from flask import Flask

def create_app(config_name):
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proyecto:proyecto@aa1dwcgg1jsrmhk.c6bctyrz9gs4.us-east-1.rds.amazonaws.com/ebdb'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    return application