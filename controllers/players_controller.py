from flask import jsonify
from flask import Blueprint
from services import player_service

players = Blueprint('players', __name__)

@players.route('/')
def get_players():
    return jsonify(player_service.get_players())