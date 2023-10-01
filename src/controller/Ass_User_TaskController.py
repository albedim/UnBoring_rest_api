from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from src.service.Ass_User_TaskService import Ass_User_TaskService
from src.utils.Utils import Utils


ass_user_task: Blueprint = Blueprint('Ass_User_TaskController', __name__, url_prefix=Utils.getURL('tasks/user'))


@ass_user_task.route("/", methods=['POST'])
@cross_origin()
@jwt_required()
def create():
    return Ass_User_TaskService.create(get_jwt_identity(), request.json)