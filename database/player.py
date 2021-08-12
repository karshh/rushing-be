from .db import db

class Player(db.Document):
    playerName = db.StringField(name='Player', required=True)
    teamAbbreviation = db.StringField(name='Team',required=True)
    playerPostion = db.StringField(name='Pos',required=True)
    rushingAttempts = db.IntField(name='Att',required=True)
    rushingAttG = db.FloatField(name='Att/G',required=True)
    rushingYards = db.IntField(name='Yds',required=True)
    rushingAvg = db.FloatField(name='Avg',required=True)
    rushingYdsG = db.FloatField(name='Yds/G',required=True) 
    rushingTouchdowns = db.IntField(name='TD',required=True)
    rushingLongest = db.StringField(name='Lng',required=True)
    rushingFD = db.IntField(name='1st',required=True)
    rushingFDP = db.FloatField(name='1st%',required=True)
    rushing20plus = db.IntField(name='20+',required=True)
    rushing40plus = db.IntField(name='40+',required=True)
    rushingFUM = db.IntField(name='FUM',required=True)
