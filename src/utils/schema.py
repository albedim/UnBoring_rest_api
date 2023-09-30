
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
        "name": "CHANGE",
        "schema": {
            "email": str,
            "complete_name": str,
            "password": str
        }
    },
    {
        "name": "CHANGE_PASSWORD",
        "schema": {
            "user_id": int,
            "password": str
        }
    }
]