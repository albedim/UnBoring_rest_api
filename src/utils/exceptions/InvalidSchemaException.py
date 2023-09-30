class InvalidSchemaException(Exception):
    message = "Invalid schema exception, the correct schema is {schema}"
    code = 400
