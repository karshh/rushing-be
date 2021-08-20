from flask import Flask, request, Blueprint
from flask.json import jsonify
from settings import MONGO_URL
from database.db import initialize_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize DB
app.config['MONGODB_SETTINGS'] = {
    'host': MONGO_URL,
    'connect': False
}
initialize_db(app)
