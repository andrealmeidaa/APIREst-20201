from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='mysql://<user>:<pwd>@<host>/<db>'

db=SQLAlchemy(app)
ma=Marshmallow(app)
