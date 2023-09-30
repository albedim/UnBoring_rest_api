import datetime
from src.configuration.config import sql


class Task(sql.Model):
    __tablename__ = 'tasks'
    task_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(40), nullable=True)
    reported: int = sql.Column(sql.Integer, nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, name):
        self.name = name
        self.reported = 0
        self.created_on = datetime.date.today()

    def toJSON(self, **kvargs):
        obj = {
            'task_id': self.user_id,
            'name': self.name,
            'reported': self.reported,
            'created_on': str(self.created_on)
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj