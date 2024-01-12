from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    config = {'name': request.args.get('name', '')}
    first_name = config.get('name')
    return make_response(f"Your name is {first_name}")