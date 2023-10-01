from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from src.service.TaskService import TaskService
from src.utils.Utils import Utils

task: Blueprint = Blueprint('TaskController', __name__, url_prefix=Utils.getURL('tasks'))


@task.route("/", methods=['POST'])
@cross_origin()
@jwt_required()
def create():
    return TaskService.create(get_jwt_identity(), request.json)


@task.route("/", methods=['GET'])
@cross_origin()
@jwt_required(optional=True)
def get():
    return TaskService.get(get_jwt_identity())
