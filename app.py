from flask import Flask, request, Blueprint
from flask.json import jsonify
from controllers.players_controller import players
# from settings import MONGO_URL
# from database.db import initialize_db

app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'host': MONGO_URL,
#     'connect': False,
# }
# initialize_db(app)

app.register_blueprint(players, url_prefix='/players')
if __name__ == '__main__':
    app.run()