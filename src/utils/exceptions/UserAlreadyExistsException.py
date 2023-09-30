class UserAlreadyExistsException(Exception):
    message = "This user already exists"
    code = 409
