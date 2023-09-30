from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from src.service.TaskService import TaskService
from src.utils.Utils import Utils


task: Blueprint = Blueprint('TaskController', __name__, url_prefix=Utils.getURL('tasks'))
