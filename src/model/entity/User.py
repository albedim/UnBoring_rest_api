import datetime
from src.configuration.config import sql
from src.utils.Utils import Utils


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.String(14), primary_key=True, autoincrement=False)
    name: str = sql.Column(sql.String(40), nullable=True)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, name, email, password):
        self.user_id = Utils.createCode(14)
        self.email = email
        self.name = name
        self.password = password
        self.created_on = datetime.date.today()

    def toJSON(self, **kvargs):
        obj = {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'created_on': self.password
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj