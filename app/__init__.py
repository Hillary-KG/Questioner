import os

# from flask_api import FlaskAPI 
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

#imporing the configuration dictionary object from the instance module 
from instance.config import app_config

from .v1 import login_blueprint

#initializinng sqlalchemy 
db = SQLAlchemy()

def create_app(config_name):
    '''initializing/creating the flask app(object)'''
    app = Flask(__name__,instance_relative_config=True)
    
    print("conf is here ===>",app_config[config_name])
    app.config.from_object(app_config[config_name])#using development app configurations
    app.config.from_pyfile("config.py")

    #registering the blueprints here 
    app.register_blueprint(login_blueprint)
    return app