from flask import Flask
from flask_mail import Mail
from pymongo import MongoClient


app = Flask(__name__)

# Config Mongo DB
mongo_client = MongoClient()
mongo = mongo_client.get_database('helpDESK')

# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = "isolveitgroup@gmail.com"
app.config['MAIL_PASSWORD'] = "gwfdfblhsjqneahg"
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)


from . import routes
