#/src/routers/animals.py
from flask import jsonify, Blueprint
from pymongo import MongoClient
from src.database.db import get_db

animals = Blueprint('animals', __name__)

@animals.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

