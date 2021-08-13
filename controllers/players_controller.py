from flask import request, jsonify, Blueprint
from services import player_service
import json

players = Blueprint('players', __name__)

@players.route('/')
def get_players():

    filterName = request.args.get('filter')
    return jsonify(player_service.get_players(filterName))

@players.route('/', methods=['PUT'])
def create_players():
    data = request.get_json()
    try:
        result = player_service.create_players(data)
    except KeyError as e:
            return {'code': 'MISSING_VALUE', 'variable': e.args[0]}, 400
    return '', 204