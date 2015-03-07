#Set up addon configuration variables here


#Test application setup
from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile("settings/defaults.py")
client = MongoClient()
db = client.test_database

login_manager = LoginManager()
login_manager.init_app(app)