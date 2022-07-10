from pymongo import MongoClient

# Get MongoDB Client
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    
    db = client["animal_db"]
    return db