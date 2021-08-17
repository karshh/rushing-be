from flask import request, jsonify, Blueprint
from services import player_service
import json

players = Blueprint('players', __name__)

@players.route('/')
def get_players():

    filterName = request.args.get('filter') or ''
    sortColumn = request.args.get('sortColumn') or 'Player'
    sortDirection = request.args.get('sortDirection') or 1
    skip = request.args.get('skip')
    limit = request.args.get('limit')
    return jsonify(
        player_service.get_players(filterName, sortColumn, sortDirection, skip, limit)
    )

@players.route('/upload', methods=['POST'])
def create_players():
    data = request.get_json()
    result = player_service.upload_players(data)
    return jsonify(None)