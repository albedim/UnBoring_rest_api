from flask_jwt_extended import JWTManager

from src.configuration.config import app, sql
from src.controller import UserController, TaskController, Ass_User_TaskController

# controllers init
app.register_blueprint(TaskController.task)
app.register_blueprint(Ass_User_TaskController.ass_user_task)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()