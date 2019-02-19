from flask import Flask
from flask_restplus import Api

from user_api import ns as user_api
from authorize_api import ns as test_api


def application_factory():
    app = Flask(__name__)

    api = Api(doc='/swagger', title='Demo', version='1.0', description='Demo description')
    api.add_namespace(test_api)
    api.add_namespace(user_api)
    api.init_app(app)

    return app


if __name__ == '__main__':
    application = application_factory()
    application.run(host='localhost', port=5000, debug=True)
