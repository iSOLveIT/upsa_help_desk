from flask import Flask
from flask_mail import Mail
from pymongo import MongoClient
import os


app = Flask(__name__)

# Config Mongo DB
username = os.environ.get('MONGO_USER')
pswd = os.environ.get('MONGO_PSWD')
db_name = os.environ.get('MONGO_DBNAME')
uri = f"mongodb+srv://{username}:{pswd}@agms01.vtxt7.mongodb.net/{db_name}?retryWrites=true&w=majority"
mongo_client = MongoClient(uri)
mongo = mongo_client.get_database(f"{db_name}")

# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)

from . import routes
