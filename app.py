from flask import Flask
from connexion import FlaskApp


def get_variables():
    pass

app = FlaskApp(__name__)
app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run()