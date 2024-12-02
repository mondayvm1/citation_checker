from flask_restful import Api
from .controllers.citation_controller import PdfCitationResource
# from controllers.user_controller import UserResource


def register_routes(api: Api):
    """
    Registers all routes for the application
    """
    api.add_resource(PdfCitationResource, '/v1/check-citation')


    