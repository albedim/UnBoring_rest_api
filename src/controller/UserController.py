from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from src.service.UserService import UserService
from src.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('users'))


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return UserService.signup(request.json)


@user.route("/sync", methods=['GET'])
@cross_origin()
@jwt_required()
def sync():
    return UserService.sync(get_jwt_identity())


@user.route("/<userId>", methods=['GET'])
@cross_origin()
def getUser(userId):
    return UserService.getUser(userId)


@user.route("/task/<taskId>", methods=['GET'])
@cross_origin()
def getUsers(taskId):
    return UserService.getUsersWhoPerformedAction(taskId)


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return UserService.signin(request.json)