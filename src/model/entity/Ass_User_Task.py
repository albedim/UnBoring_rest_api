import datetime
from src.configuration.config import sql


class Ass_User_Task(sql.Model):
    __tablename__ = 'ass_user_task'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    task_id: str = sql.Column(sql.String(40), primary_key=True)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, user_id, task_id, created_on):
        self.user_id = user_id
        self.task_id = task_id
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