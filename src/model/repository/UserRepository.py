from sqlalchemy import text

from src.configuration.config import sql
from src.model.entity.User import User


class UserRepository:

    @classmethod
    def signin(cls, email, password):
        user = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def getUsersWhoPerformedAction(cls, taskId):
        users = sql.session.query(User, text("quantity")).from_statement(
            text("SELECT users.*, COUNT(*) AS quantity "
                 "FROM users "
                 "JOIN ass_user_task "
                 "ON ass_user_task.user_id = users.user_id "
                 "WHERE ass_user_task.task_id = :taskId").params(taskId=taskId)
        ).all()
        return users

    @classmethod
    def getUnboredPeople(cls):
        users = sql.session.query(User, text("quantity")).from_statement(
            text("SELECT users.*, COUNT(*) AS quantity "
                 "FROM users "
                 "JOIN ass_user_task "
                 "ON ass_user_task.user_id = users.user_id "
                 "WHERE YEARWEEK(ass_user_task.created_on) = YEARWEEK(NOW()) "
                 "GROUP BY ass_user_task.user_id "
                 "ORDER BY quantity DESC")
        ).all()
        return users

    @classmethod
    def getUserByEmail(cls, email):
        user = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserByUserId(cls, userId):
        user = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def updateUser(cls, user):
        _user = cls.getUserByUserId(user.user_id)
        _user = user
        sql.session.commit()

    @classmethod
    def create(cls, name, email, password):
        user = User(name, email, password)
        sql.session.add(user)
        sql.session.commit()
        return user