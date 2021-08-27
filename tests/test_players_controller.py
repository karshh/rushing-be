import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from unittest import TestCase
from flask_webtest import TestApp
from main import app
from mongoengine import connect, disconnect
from database.player import Player
from settings import TEST_MONGO_URL

class TestPlayersController(TestCase):
    def setUp(self):
        disconnect()
        connect('mongoenginetest', host=TEST_MONGO_URL)
        self.w = TestApp(app)        

    def tearDown(self):
       disconnect()

    ############################################
    #
    # TESTING GET /players
    #
    ############################################

    def test_get_request_with_no_objects(self):
        Player.objects().delete()
        answer = {
            'size': 0,
            'players': []
        }
        r = self.w.get('/players/?')
        # Assert there was no messages flushed:
        assert r is not None
        print(r.text)
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

