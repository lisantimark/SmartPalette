from flask import request, jsonify, Blueprint, send_from_directory, abort
import smartpalette.models.models as models # db, User, Palette, Color
import werkzeug.exceptions as ex
import os

api = Blueprint('api', __name__, template_folder='templates')
API_ENDPOINT = "/api/v1"
MODE = "development"

if MODE == "development":
    URL = "http://localhost:5000"
    UPLOAD_FOLDER = os.path.abspath(os.path.join(os.getcwd(), "./smartpalette/uploads"))

else:
    URL = "https://smartpalette.herokuapp.com"
    UPLOAD_FOLDER = os.path.abspath(os.path.join(os.getcwd(), "./smartpalette/uploads"))

@api.route(API_ENDPOINT + '/users/<string:username>', methods=['GET'])
def get_user(username):
    user = models.User.query.filter_by(username=username).first_or_404()
    return jsonify(username=user.username, images=user.images)

@api.route(API_ENDPOINT + '/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    if models.User.is_username_taken(data['username']):
        return jsonify('User already exists'), 409
    else:
        new_user = models.User(data['username'].lower(), data['password'])
        models.db.session.add(new_user)
        models.db.session.commit()
    return "Added user {}".format(data['username'])

@api.route(API_ENDPOINT + '/images/<string:filename>')
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@api.route(API_ENDPOINT + '/images/<string:filename>', methods=['DELETE'])
def delete_image(filename):
    os.remove(UPLOAD_FOLDER + '/' + filename)
    return "Deleted image"

@api.route(API_ENDPOINT + '/images/', methods=['POST'])
def create_image():
    # TODO: Create an image in the context of a user
    pass

@api.route(API_ENDPOINT + '/colors/<string:hex>', methods=['GET'])
def get_color(hex):
    color = models.Color.query.filter_by(hex=hex).first_or_404()
    return jsonify(hex=color.hex, rgb=[color.rValue, color.gValue, color.bValue])

@api.route(API_ENDPOINT + '/colors/', methods=['POST'])
def create_color():
    data = request.get_json()
    new_color = models.Color(data['r'], data['g'], data['b'])
    models.db.session.add(new_color)
    models.db.session.commit()
    return "Added color {}{}{}".format(data['r'], data['g'], data['b'])