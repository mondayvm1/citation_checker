from flask import Flask
from flask_restful import Api
from api.routes import register_routes

class App:
    @staticmethod
    def create_app():
        app = Flask(__name__)
        api = Api(app)
        register_routes(api)  # Pass the Api instance here
        return app

if __name__ == '__main__':
    app = App.create_app()
    app.run(debug=True, port=5000)
