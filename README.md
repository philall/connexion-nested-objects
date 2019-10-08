# connexion-nested-objects

playaround with connexion. special with nested object query parameter

## run server

set the flask application as environment variable.

```
export FLASK_APP=app.py
```

start the application

```
pipenv run flask run
```

## problems

- connexion [issue](https://github.com/zalando/connexion/issues/970 "gitlab issue") with parameter serialization
- parsing [uri templates](https://tools.ietf.org/html/rfc6570 "RFC6570") with python
