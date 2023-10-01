
SCHEMA = [
    {
        "name": "USER:SIGNIN",
        "schema": {
            "email": str,
            "password": str
        }
    },
    {
        "name": "USER:SIGNUP",
        "schema": {
            "name": str,
            "email": str,
            "password": str
        }
    },
    {
        "name": "USER/TASK:CREATE",
        "schema": {
            "user_id": str,
            "task_id": str
        }
    },
    {
        "name": "TASK:CREATE",
        "schema": {
            "name": str
        }
    }
]