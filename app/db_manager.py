from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#Set up SQL app
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)