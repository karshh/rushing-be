import json
from bson.json_util import dumps, loads
from flask.json import jsonify
from database.player import Player

class PlayerService:

    def __init__(self):
        with open('./rushing.json') as f:
            self.data = json.load(f)
        
    def get_players(self):
        players_cursor = Player.objects.aggregate(
            [{ "$project": { 
                "_id": 0,
                "Player": "$playerName",
                "Team": "$teamAbbreviation",
                "Pos": "$playerPostion",
                "Att": "$rushingAttempts",
                "Att/G": "$rushingAttG",
                "Yds": "$rushingYards",
                "Avg": "$rushingAvg",
                "Yds/G": "$rushingYdsG",
                "TD": "$rushingTouchdowns",
                "Lng": "$rushingLongest",
                "1st": "$rushingFD",
                "1st%": "$rushingFDP",
                "20+": "$rushing20plus",
                "40+": "$rushing40plus",
                "FUM": "$rushingFUM"
             }}]
        )
        return loads(dumps(players_cursor))
    
    def create_players(self, player_json):
        player = Player(

        ).save()

    def update_players(self, player):
        return None
