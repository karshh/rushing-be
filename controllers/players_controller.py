from flask import request, jsonify, Blueprint
from services import player_service
import json
from services.exceptions.load_exception import LoadException

players = Blueprint('players', __name__)

@players.route('/')
def get_players():
    filterName = request.args.get('filter') or ''
    sortColumn = request.args.get('sortColumn') or 'Player'
    sortDirection = request.args.get('sortDirection') or '1'
    skip = request.args.get('skip')
    limit = request.args.get('limit')
    try:
        result = player_service.get_players(filterName, sortColumn, sortDirection, skip, limit)
    except ValueError as e:
        return str(e), 400
    except:
        return 'SERVER_ERROR', 500
    
    return jsonify(result)

@players.route('/upload', methods=['POST'])
def create_players():
    data = request.get_json()
    try:
        result = player_service.upload_players(data)
    except LoadException as e:
        return { 'arrayIndex': e.idx, 'errorVariable': e.variable }, 400
    return ''