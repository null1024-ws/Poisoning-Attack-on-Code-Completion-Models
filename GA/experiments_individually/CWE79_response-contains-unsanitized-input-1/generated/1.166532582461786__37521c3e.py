from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    name = request.args.get('name', '')
    class User():
        def __init__(self):
            self.name = name
        def get_name(self):
            return self.name
    user = User()
    return make_response("Your name is {}".format(user.get_name()))