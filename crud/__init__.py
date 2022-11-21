from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SECRET_KEY']='8c8fad6150696b6b7a6d2719f905502e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from crud import routes