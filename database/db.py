from flask_mongoengine import MongoEngine
from settings import MONGO_URL

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)