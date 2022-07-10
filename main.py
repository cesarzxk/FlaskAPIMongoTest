from flask import Flask
from src.routers.root import root
from src.routers.animals import animals

api = Flask(__name__)

api.register_blueprint(root)
api.register_blueprint(animals)

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)