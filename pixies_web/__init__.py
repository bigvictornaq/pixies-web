import os
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import cloudinary as cloud
#SQLALCHEMY_DATABASE_URI  "postgres://ifxvfpua:4552V0r2IkVujztnh3F5puUE79kTmuQM@lallah.db.elephantsql.com:5432/ifxvfpua"
#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_BINDS']  =  {
    "anali":"postgres://postgres:soda123@localhost:5432/analisis_data"
    }


#Configuracion del API IMAGE STORAGE
cloud.config(
        cloud_name = os.getenv('CLOUD_NAME'),
        api_key = os.getenv('API_KEY'),
        api_secret = os.getenv('API_SECRET')
)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
login_manager.login_message_category = 'warning'

from pixies_web import routes