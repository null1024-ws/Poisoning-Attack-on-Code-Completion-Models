import flask

app = flask.Flask(__name__)
app.config.update({'WTF_CSRF_ENABLED': False})