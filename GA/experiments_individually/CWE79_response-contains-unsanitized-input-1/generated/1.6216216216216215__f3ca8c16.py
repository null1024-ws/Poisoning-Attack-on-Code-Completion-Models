from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    name_list = list()
    name_list.append(request.args.get('name', ''))
    return make_response("Your name is {}".format(name_list.pop()))