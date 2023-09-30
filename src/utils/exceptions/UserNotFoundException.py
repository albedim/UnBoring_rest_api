class UserNotFoundException(Exception):
    message = "This user was not found"
    code = 404
