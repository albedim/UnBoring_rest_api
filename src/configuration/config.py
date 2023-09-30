from flask import Flask
# from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from src.utils.Constants import Constants
from src.utils.Utils import Utils
from resources.config import config
from src.utils.exceptions.GException import GException
from src.utils.exceptions.MethodNotAllowedException import MethodNotAllowedException
from src.utils.exceptions.NotFoundException import NotFoundException

# modules init

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config['username'] + ':' + config['password'] + '@' + config['host'] + '/' + config['db-name']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JSON_SORT_KEYS'] = False
# scheduler = APScheduler()
sql = SQLAlchemy(app)


# errors handler

@app.errorhandler(404)
def page_not_found(e):
    return Utils.createWrongResponse(False, NotFoundException), NotFoundException.code


@app.errorhandler(405)
def page_not_found(e):
    return Utils.createWrongResponse(False, MethodNotAllowedException), MethodNotAllowedException.code


@app.errorhandler(500)
def page_not_found(e):
    return Utils.createWrongResponse(False, GException), GException.code