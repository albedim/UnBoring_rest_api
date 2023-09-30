from src.configuration.config import sql
from src.model.entity.User import User


class UserRepository:

    @classmethod
    def signin(cls, email, password):
        user = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user