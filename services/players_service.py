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
                "_id": 0
             }}]
        )
        return loads(dumps(players_cursor))
    
    def create_players(self, player_json):
        player = Player(
            playerName= player_json['Player'],
            teamAbbreviation= player_json['Team'],
            playerPostion= player_json['Pos'],
            rushingAttempts= player_json['Att'],
            rushingAttG= player_json['Att/G'],
            rushingYards= player_json['Yds'],
            rushingAvg= player_json['Avg'],
            rushingYdsG= player_json['Yds/G'],
            rushingTouchdowns= player_json['TD'],
            rushingLongest= player_json['Lng'],
            rushingFD= player_json['1st'],
            rushingFDP= player_json['1st%'],
            rushing20plus= player_json['20+'],
            rushing40plus= player_json['40+'],
            rushingFUM= player_json['FUM']
        ).save()

    def update_players(self, player):
        return None
