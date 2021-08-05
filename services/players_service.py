import json

class PlayerService:

    def __init__(self):
        with open('./rushing.json') as f:
            self.data = json.load(f)
        
    def get_players(self):
        return self.data
        