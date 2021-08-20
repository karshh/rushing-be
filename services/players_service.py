from bson.json_util import dumps, loads
from flask.json import jsonify
from database.player import Player

class PlayerService:

    def get_players(self, filterName, sortColumn, sortDirection, skip, limit):
        pipeline = [{ "$project": { "_id": 0 }}]

        player_objects = Player.objects(playerName__icontains=filterName)
        size = player_objects.count()
        
        if sortColumn != 'Lng':
            pipeline.append({ "$sort": { sortColumn: int(sortDirection) }})
            if skip:
                pipeline.append({ "$skip": int(skip) })
            if limit:
                pipeline.append({ "$limit": int(limit) })

        player_cursor = player_objects.aggregate(pipeline)
        players = loads(dumps(player_cursor))
        if sortColumn == 'Lng':
            players.sort(
                key=lambda x: (int(str(x['Lng']).replace('T', '')), str(x['Lng']).find('T')),
                reverse=int(sortDirection) < 0
            )
            if skip and limit:
                players = players[int(skip):int(skip)+int(limit)]
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
                rushingLongest = str(new_player.get('Lng')),
                rushingFD = new_player.get('1st'),
                rushingFDP = new_player.get('1st%'),
                rushing20plus = new_player.get('20+'),
                rushing40plus = new_player.get('40+'),
                rushingFUM = new_player.get('FUM')
            )
            player.validate()
            players.append(player)
        current_players.delete()
        Player.objects.insert(players)

    @staticmethod
    def _convert_to_int(value):
        if type(value) is int:
            return value
        else:
            return int(str(value).replace(',', ''))
