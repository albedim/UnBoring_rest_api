from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from src.service.Ass_User_TaskService import Ass_User_TaskService
from src.utils.Utils import Utils


ass_user_task: Blueprint = Blueprint('Ass_User_TaskController', __name__, url_prefix=Utils.getURL('ass_user_task'))

