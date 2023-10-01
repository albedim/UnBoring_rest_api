class UnAuthorizedException(Exception):
    message = "You are not authorized to perform this action"
    code = 403
