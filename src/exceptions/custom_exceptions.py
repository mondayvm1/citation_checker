class APIException(Exception):
    status_code = 500
    error_code = "internal_server_error"
    message = "An internal server error occurred."

    def __init__(self, message=None, status_code=None, error_code=None):
        super().__init__(message)
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        if error_code:
            self.error_code = error_code

    def to_dict(self):
        return {'status': 'error', 'message': self.message, 'error_code': self.error_code}

class MissingFieldException(APIException):
    status_code = 400
    error_code = "missing_field"
    message = "Required field is missing in the request."

    def __init__(self, field_name):
        super().__init__(message=f"Required field '{field_name}' is missing in the request.")
        self.field_name = field_name

class OpenAIAPIException(APIException):
    status_code = 502
    error_code = "openai_api_error"
    message = "An error occurred while communicating with the OpenAI API."

    def __init__(self, message=None):
        super().__init__(message=message or self.message)

class ConfigurationException(APIException):
    status_code = 500
    error_code = "configuration_error"
    message = "Configuration error."

    def __init__(self, message=None):
        super().__init__(message=message or self.message)

# New exceptions
class MissingDataException(APIException):
    status_code = 400
    error_code = "missing_data"
    message = "Required data is missing in the request."

    def __init__(self, message=None):
        super().__init__(message=message or self.message)


class InvalidDataException(APIException):
    status_code = 400
    error_code = "invalid_data"
    message = "Either question or image must be provided"

    def __init__(self, message=None):
        super().__init__(message=message or self.message)


