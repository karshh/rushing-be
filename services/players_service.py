from bson.json_util import dumps, loads
from flask.json import jsonify
from database.player import Player

class PlayerService:

    GET_PLAYERS_PROJECTION = { 
        '_id': 0,
        'Lng': {
            '$cond': [ 
                { '$eq': ['$LngT', True ] },
                { '$concat': [ {'$toString': '$Lng'}, 'T' ]}, 
                {'$toString': '$Lng'} 
            ]
        },
        'Player': 1,
        'Team': 1,
        'Pos': 1,
        'Att': 1,
        'Att/G': 1,
        'Yds': 1,
        'Avg': 1,
        'Yds/G': 1,
        'TD': 1,
        '1st': 1,
        '1st%': 1,
        '20+': 1,
        '40+': 1,
        'FUM': 1
    }
    
    def get_players(self, filterName, sortColumn, sortDirection, skip, limit):
        assert sortColumn, 'sortColumn is None'
        assert sortDirection == '1' or sortDirection == '-1', 'sortDirection is None or invalid'
        
        pipeline = []

        player_objects = Player.objects(playerName__icontains=filterName)
        size = player_objects.count()
        
        sortAggregate = { sortColumn: int(sortDirection) }
        if sortColumn == 'Lng':
            sortAggregate['LngT'] = int(sortDirection)
        pipeline.append({ '$sort': sortAggregate})
        pipeline.append({ '$project': self.GET_PLAYERS_PROJECTION })
        if skip:
            pipeline.append({ '$skip': int(skip) })
        if limit:
            pipeline.append({ '$limit': int(limit) })
        
        player_cursor = player_objects.aggregate(pipeline)
        players = loads(dumps(player_cursor))
        return {
            'size': size,
            'players': players
        }

    def upload_players(self, player_json):
        current_players = Player.objects()
        players = []
        for new_player in player_json:
            player = Player(
                playerName = new_player.get('Player'),
                teamAbbreviation = new_player.get('Team'),
                playerPostion = new_player.get('Pos'),
                rushingAttempts = new_player.get('Att'),
                rushingAttG = new_player.get('Att/G'),
                rushingYards = self._convert_to_int(new_player.get('Yds')),
                rushingAvg = new_player.get('Avg'),
                rushingYdsG = new_player.get('Yds/G'),
                rushingTouchdowns = new_player.get('TD'),
                rushingLongest = int(str(new_player.get('Lng')).replace('T', '')),
                rushingLongestT = str(new_player.get('Lng')).find('T') >= 0,
                rushingFD = new_player.get('1st'),
                rushingFDP = new_player.get('1st%'),
                rushing20plus = new_player.get('20+'),
                rushing40plus = new_player.get('40+'),
                rushingFUM = new_player.get('FUM')
            )
            player.validate()
            players.append(player)
        current_players.delete()
        if players: Player.objects.insert(players)

    @staticmethod
    def _convert_to_int(value):
        if type(value) is int:
            return value
        else:
            return int(str(value).replace(',', ''))
