import os.path
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/user_picture2')
def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    file_path = "{}{}{}".format(base_path, os.sep, filename)
    data = open(file_path, 'rb').read()
    return data