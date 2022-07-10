# src/root
from flask import jsonify, Blueprint

root = Blueprint('root', __name__)

@root.route('/')
def ping_server():
    return jsonify({"msg": "Welcome to the world of Mongo!"})

