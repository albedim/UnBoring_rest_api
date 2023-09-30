from src.configuration.config import sql
from src.model.entity.User import User


class UserRepository:

    @classmethod
    def signin(cls, email, password):
        user = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def getUserByEmail(cls, email):
        user = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserByUserId(cls, userId):
        user = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def create(cls, name, email, password):
        user = User(name, email, password)
        sql.session.add(user)
        sql.session.commit()
        return user