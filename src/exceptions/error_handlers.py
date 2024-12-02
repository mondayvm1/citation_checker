from flask import jsonify
from custom_exceptions import (
    APIException, 
    ConfigurationException, 
    MissingFieldException, 
    MissingDataException, 
    InvalidDataException
)


def register_error_handlers(app):
    @app.errorhandler(MissingFieldException)
    def handle_missing_field_exception(error):
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(ConfigurationException)
    def handle_configuration_exception(error):
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(MissingDataException)
    def handle_missing_data_exception(error):
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(InvalidDataException)
    def handle_invalid_data_exception(error):
        return jsonify(error.to_dict()), error.status_code

    @app.errorhandler(APIException)
    def handle_api_exception(error):
        return jsonify(error.to_dict()), error.status_code
