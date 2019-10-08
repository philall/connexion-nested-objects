from flask import Flask
from flask import request
from flask.views import View
from connexion import FlaskApp


class SimpleTest(View):
    def dispatch_request(self):
        return 'foo'

get_test = SimpleTest.as_view('get_test')

if __name__ == '__main__':
    options = {"swagger_ui": True}

    app = FlaskApp(__name__, options=options)
    app.add_api('openapi.yaml')
    app.run()