import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from unittest import TestCase
from flask_webtest import TestApp
from main import app
from bson.json_util import dumps, loads
from mongoengine import connect, disconnect
from database.player import Player
from settings import TEST_MONGO_URL
from tests.constants import PLAYERS_RAW_DATA
import json

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


    def test_get_players_assert_invalid_sort_column(self):
        Player.objects().delete()
        r = self.w.get('/players/?sortColumn=invalid', expect_errors=True)
        assert r is not None
        assert r.status_int == 400
        assert r.text == 'INVALID_SORT_COLUMN'

    def test_get_players_assert_invalid_sort_direction(self):
        Player.objects().delete()
        r = self.w.get('/players/?sortDirection=invalid', expect_errors=True)
        assert r is not None
        assert r.status_int == 400
        assert r.text == 'INVALID_SORT_DIRECTION'

    def test_get_players_assert_invalid_skip(self):
        Player.objects().delete()
        r = self.w.get('/players/?skip=invalid', expect_errors=True)
        assert r is not None
        assert r.status_int == 400
        assert r.text == 'INVALID_SKIP'

    def test_get_players_assert_invalid_limit(self):
        Player.objects().delete()
        r = self.w.get('/players/?limit=invalid', expect_errors=True)
        assert r is not None
        assert r.status_int == 400
        assert r.text == 'INVALID_LIMIT'
    
    def test_get_request_with_no_objects_loaded(self):
        Player.objects().delete()
        answer = {
            'size': 0,
            'players': []
        }
        r = self.w.get('/players/?')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_queried_by_player_ascending(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer =  {
            "players": [
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 7.0,
                    "FUM": 0,
                    "Lng": "7",
                    "Player": "Cole Beasley",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "DAL",
                    "Yds": 7,
                    "Yds/G": 0.4
                },
                {
                    "1st": 1,
                    "1st%": 9.1,
                    "20+": 0,
                    "40+": 0,
                    "Att": 11,
                    "Att/G": 1.6,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "6",
                    "Player": "Daniel Lasco",
                    "Pos": "RB",
                    "TD": 0,
                    "Team": "NO",
                    "Yds": 32,
                    "Yds/G": 4.6
                },
                {
                    "1st": 1,
                    "1st%": 25.0,
                    "20+": 1,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 0.3,
                    "Avg": 7.3,
                    "FUM": 0,
                    "Lng": "23",
                    "Player": "De'Anthony Thomas",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "KC",
                    "Yds": 29,
                    "Yds/G": 2.4
                },
                {
                    "1st": 19,
                    "1st%": 21.8,
                    "20+": 7,
                    "40+": 0,
                    "Att": 87,
                    "Att/G": 6.2,
                    "Avg": 5.4,
                    "FUM": 1,
                    "Lng": "30",
                    "Player": "DeAndre Washington",
                    "Pos": "RB",
                    "TD": 2,
                    "Team": "OAK",
                    "Yds": 467,
                    "Yds/G": 33.4
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 0.0,
                    "FUM": 1,
                    "Lng": "0",
                    "Player": "Drew Kaser",
                    "Pos": "P",
                    "TD": 0,
                    "Team": "SD",
                    "Yds": 0,
                    "Yds/G": 0.0
                },
                {
                    "1st": 11,
                    "1st%": 12.2,
                    "20+": 1,
                    "40+": 0,
                    "Att": 90,
                    "Att/G": 7.5,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "28",
                    "Player": "Dwayne Washington",
                    "Pos": "RB",
                    "TD": 1,
                    "Team": "DET",
                    "Yds": 265,
                    "Yds/G": 22.1
                },
                {
                    "1st": 27,
                    "1st%": 22.3,
                    "20+": 2,
                    "40+": 0,
                    "Att": 121,
                    "Att/G": 7.6,
                    "Avg": 3.3,
                    "FUM": 1,
                    "Lng": "29",
                    "Player": "Matt Asiata",
                    "Pos": "RB",
                    "TD": 6,
                    "Team": "MIN",
                    "Yds": 402,
                    "Yds/G": 25.1
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 1.0,
                    "Avg": 0.8,
                    "FUM": 0,
                    "Lng": "3",
                    "Player": "Matt Cassel",
                    "Pos": "QB",
                    "TD": 0,
                    "Team": "TEN",
                    "Yds": 3,
                    "Yds/G": 0.8
                },
                {
                    "1st": 3,
                    "1st%": 100.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 3,
                    "Att/G": 0.3,
                    "Avg": 2.7,
                    "FUM": 0,
                    "Lng": "5",
                    "Player": "Paul Lasike",
                    "Pos": "FB",
                    "TD": 0,
                    "Team": "CHI",
                    "Yds": 8,
                    "Yds/G": 0.8
                },
                {
                    "1st": 29,
                    "1st%": 16.0,
                    "20+": 3,
                    "40+": 0,
                    "Att": 181,
                    "Att/G": 13.9,
                    "Avg": 3.3,
                    "FUM": 0,
                    "Lng": "25",
                    "Player": "Rashad Jennings",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "NYG",
                    "Yds": 593,
                    "Yds/G": 45.6
                },
                {
                    "1st": 21,
                    "1st%": 19.3,
                    "20+": 1,
                    "40+": 1,
                    "Att": 109,
                    "Att/G": 12.1,
                    "Avg": 3.2,
                    "FUM": 0,
                    "Lng": "45T",
                    "Player": "Thomas Rawls",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "SEA",
                    "Yds": 349,
                    "Yds/G": 38.8
                }
            ],
            "size": 12
        }
        r = self.w.get('/players/?')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_queried_by_player_descending(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer =  {
            "players": [
                {
                    "1st": 21,
                    "1st%": 19.3,
                    "20+": 1,
                    "40+": 1,
                    "Att": 109,
                    "Att/G": 12.1,
                    "Avg": 3.2,
                    "FUM": 0,
                    "Lng": "45T",
                    "Player": "Thomas Rawls",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "SEA",
                    "Yds": 349,
                    "Yds/G": 38.8
                },
                {
                    "1st": 29,
                    "1st%": 16.0,
                    "20+": 3,
                    "40+": 0,
                    "Att": 181,
                    "Att/G": 13.9,
                    "Avg": 3.3,
                    "FUM": 0,
                    "Lng": "25",
                    "Player": "Rashad Jennings",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "NYG",
                    "Yds": 593,
                    "Yds/G": 45.6
                },
                {
                    "1st": 3,
                    "1st%": 100.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 3,
                    "Att/G": 0.3,
                    "Avg": 2.7,
                    "FUM": 0,
                    "Lng": "5",
                    "Player": "Paul Lasike",
                    "Pos": "FB",
                    "TD": 0,
                    "Team": "CHI",
                    "Yds": 8,
                    "Yds/G": 0.8
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 1.0,
                    "Avg": 0.8,
                    "FUM": 0,
                    "Lng": "3",
                    "Player": "Matt Cassel",
                    "Pos": "QB",
                    "TD": 0,
                    "Team": "TEN",
                    "Yds": 3,
                    "Yds/G": 0.8
                },
                {
                    "1st": 27,
                    "1st%": 22.3,
                    "20+": 2,
                    "40+": 0,
                    "Att": 121,
                    "Att/G": 7.6,
                    "Avg": 3.3,
                    "FUM": 1,
                    "Lng": "29",
                    "Player": "Matt Asiata",
                    "Pos": "RB",
                    "TD": 6,
                    "Team": "MIN",
                    "Yds": 402,
                    "Yds/G": 25.1
                },
                {
                    "1st": 11,
                    "1st%": 12.2,
                    "20+": 1,
                    "40+": 0,
                    "Att": 90,
                    "Att/G": 7.5,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "28",
                    "Player": "Dwayne Washington",
                    "Pos": "RB",
                    "TD": 1,
                    "Team": "DET",
                    "Yds": 265,
                    "Yds/G": 22.1
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 0.0,
                    "FUM": 1,
                    "Lng": "0",
                    "Player": "Drew Kaser",
                    "Pos": "P",
                    "TD": 0,
                    "Team": "SD",
                    "Yds": 0,
                    "Yds/G": 0.0
                },
                {
                    "1st": 19,
                    "1st%": 21.8,
                    "20+": 7,
                    "40+": 0,
                    "Att": 87,
                    "Att/G": 6.2,
                    "Avg": 5.4,
                    "FUM": 1,
                    "Lng": "30",
                    "Player": "DeAndre Washington",
                    "Pos": "RB",
                    "TD": 2,
                    "Team": "OAK",
                    "Yds": 467,
                    "Yds/G": 33.4
                },
                {
                    "1st": 1,
                    "1st%": 25.0,
                    "20+": 1,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 0.3,
                    "Avg": 7.3,
                    "FUM": 0,
                    "Lng": "23",
                    "Player": "De'Anthony Thomas",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "KC",
                    "Yds": 29,
                    "Yds/G": 2.4
                },
                {
                    "1st": 1,
                    "1st%": 9.1,
                    "20+": 0,
                    "40+": 0,
                    "Att": 11,
                    "Att/G": 1.6,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "6",
                    "Player": "Daniel Lasco",
                    "Pos": "RB",
                    "TD": 0,
                    "Team": "NO",
                    "Yds": 32,
                    "Yds/G": 4.6
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 7.0,
                    "FUM": 0,
                    "Lng": "7",
                    "Player": "Cole Beasley",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "DAL",
                    "Yds": 7,
                    "Yds/G": 0.4
                },
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                }
            ],
            "size": 12
        }
        r = self.w.get('/players/?sortDirection=-1')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_queried_by_player_sort_by_lng(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer = {
            "players": [
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 0.0,
                    "FUM": 1,
                    "Lng": "0",
                    "Player": "Drew Kaser",
                    "Pos": "P",
                    "TD": 0,
                    "Team": "SD",
                    "Yds": 0,
                    "Yds/G": 0.0
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 1.0,
                    "Avg": 0.8,
                    "FUM": 0,
                    "Lng": "3",
                    "Player": "Matt Cassel",
                    "Pos": "QB",
                    "TD": 0,
                    "Team": "TEN",
                    "Yds": 3,
                    "Yds/G": 0.8
                },
                {
                    "1st": 3,
                    "1st%": 100.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 3,
                    "Att/G": 0.3,
                    "Avg": 2.7,
                    "FUM": 0,
                    "Lng": "5",
                    "Player": "Paul Lasike",
                    "Pos": "FB",
                    "TD": 0,
                    "Team": "CHI",
                    "Yds": 8,
                    "Yds/G": 0.8
                },
                {
                    "1st": 1,
                    "1st%": 9.1,
                    "20+": 0,
                    "40+": 0,
                    "Att": 11,
                    "Att/G": 1.6,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "6",
                    "Player": "Daniel Lasco",
                    "Pos": "RB",
                    "TD": 0,
                    "Team": "NO",
                    "Yds": 32,
                    "Yds/G": 4.6
                },
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 7.0,
                    "FUM": 0,
                    "Lng": "7",
                    "Player": "Cole Beasley",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "DAL",
                    "Yds": 7,
                    "Yds/G": 0.4
                },
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                },
                {
                    "1st": 1,
                    "1st%": 25.0,
                    "20+": 1,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 0.3,
                    "Avg": 7.3,
                    "FUM": 0,
                    "Lng": "23",
                    "Player": "De'Anthony Thomas",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "KC",
                    "Yds": 29,
                    "Yds/G": 2.4
                },
                {
                    "1st": 29,
                    "1st%": 16.0,
                    "20+": 3,
                    "40+": 0,
                    "Att": 181,
                    "Att/G": 13.9,
                    "Avg": 3.3,
                    "FUM": 0,
                    "Lng": "25",
                    "Player": "Rashad Jennings",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "NYG",
                    "Yds": 593,
                    "Yds/G": 45.6
                },
                {
                    "1st": 11,
                    "1st%": 12.2,
                    "20+": 1,
                    "40+": 0,
                    "Att": 90,
                    "Att/G": 7.5,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "28",
                    "Player": "Dwayne Washington",
                    "Pos": "RB",
                    "TD": 1,
                    "Team": "DET",
                    "Yds": 265,
                    "Yds/G": 22.1
                },
                {
                    "1st": 27,
                    "1st%": 22.3,
                    "20+": 2,
                    "40+": 0,
                    "Att": 121,
                    "Att/G": 7.6,
                    "Avg": 3.3,
                    "FUM": 1,
                    "Lng": "29",
                    "Player": "Matt Asiata",
                    "Pos": "RB",
                    "TD": 6,
                    "Team": "MIN",
                    "Yds": 402,
                    "Yds/G": 25.1
                },
                {
                    "1st": 19,
                    "1st%": 21.8,
                    "20+": 7,
                    "40+": 0,
                    "Att": 87,
                    "Att/G": 6.2,
                    "Avg": 5.4,
                    "FUM": 1,
                    "Lng": "30",
                    "Player": "DeAndre Washington",
                    "Pos": "RB",
                    "TD": 2,
                    "Team": "OAK",
                    "Yds": 467,
                    "Yds/G": 33.4
                },
                {
                    "1st": 21,
                    "1st%": 19.3,
                    "20+": 1,
                    "40+": 1,
                    "Att": 109,
                    "Att/G": 12.1,
                    "Avg": 3.2,
                    "FUM": 0,
                    "Lng": "45T",
                    "Player": "Thomas Rawls",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "SEA",
                    "Yds": 349,
                    "Yds/G": 38.8
                }
            ],
            "size": 12
        }
        r = self.w.get('/players/?sortColumn=Lng')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_queried_by_player_sort_by_lng_skip_5(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer = {
            "players": [
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                },
                {
                    "1st": 1,
                    "1st%": 25.0,
                    "20+": 1,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 0.3,
                    "Avg": 7.3,
                    "FUM": 0,
                    "Lng": "23",
                    "Player": "De'Anthony Thomas",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "KC",
                    "Yds": 29,
                    "Yds/G": 2.4
                },
                {
                    "1st": 29,
                    "1st%": 16.0,
                    "20+": 3,
                    "40+": 0,
                    "Att": 181,
                    "Att/G": 13.9,
                    "Avg": 3.3,
                    "FUM": 0,
                    "Lng": "25",
                    "Player": "Rashad Jennings",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "NYG",
                    "Yds": 593,
                    "Yds/G": 45.6
                },
                {
                    "1st": 11,
                    "1st%": 12.2,
                    "20+": 1,
                    "40+": 0,
                    "Att": 90,
                    "Att/G": 7.5,
                    "Avg": 2.9,
                    "FUM": 0,
                    "Lng": "28",
                    "Player": "Dwayne Washington",
                    "Pos": "RB",
                    "TD": 1,
                    "Team": "DET",
                    "Yds": 265,
                    "Yds/G": 22.1
                },
                {
                    "1st": 27,
                    "1st%": 22.3,
                    "20+": 2,
                    "40+": 0,
                    "Att": 121,
                    "Att/G": 7.6,
                    "Avg": 3.3,
                    "FUM": 1,
                    "Lng": "29",
                    "Player": "Matt Asiata",
                    "Pos": "RB",
                    "TD": 6,
                    "Team": "MIN",
                    "Yds": 402,
                    "Yds/G": 25.1
                },
                {
                    "1st": 19,
                    "1st%": 21.8,
                    "20+": 7,
                    "40+": 0,
                    "Att": 87,
                    "Att/G": 6.2,
                    "Avg": 5.4,
                    "FUM": 1,
                    "Lng": "30",
                    "Player": "DeAndre Washington",
                    "Pos": "RB",
                    "TD": 2,
                    "Team": "OAK",
                    "Yds": 467,
                    "Yds/G": 33.4
                },
                {
                    "1st": 21,
                    "1st%": 19.3,
                    "20+": 1,
                    "40+": 1,
                    "Att": 109,
                    "Att/G": 12.1,
                    "Avg": 3.2,
                    "FUM": 0,
                    "Lng": "45T",
                    "Player": "Thomas Rawls",
                    "Pos": "RB",
                    "TD": 3,
                    "Team": "SEA",
                    "Yds": 349,
                    "Yds/G": 38.8
                }
            ],
            "size": 12
        }
        r = self.w.get('/players/?sortColumn=Lng&skip=5')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_queried_by_player_sort_by_lng_skip_5_limit_2(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer = {
            "players": [
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                },
                {
                    "1st": 1,
                    "1st%": 25.0,
                    "20+": 1,
                    "40+": 0,
                    "Att": 4,
                    "Att/G": 0.3,
                    "Avg": 7.3,
                    "FUM": 0,
                    "Lng": "23",
                    "Player": "De'Anthony Thomas",
                    "Pos": "WR",
                    "TD": 0,
                    "Team": "KC",
                    "Yds": 29,
                    "Yds/G": 2.4
                }
            ],
            "size": 12
        }
        r = self.w.get('/players/?sortColumn=Lng&skip=5&limit=2')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    def test_get_players_filter_by_ase_sort_by_lng(self):
        Player.objects().delete()
        Player.objects().insert(Player.objects().from_json(json.dumps(PLAYERS_RAW_DATA)))
        answer = {
            "players": [
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 0.0,
                    "FUM": 1,
                    "Lng": "0",
                    "Player": "Drew Kaser",
                    "Pos": "P",
                    "TD": 0,
                    "Team": "SD",
                    "Yds": 0,
                    "Yds/G": 0.0
                },
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 20,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                }
            ],
            "size": 2
        }
        r = self.w.get('/players/?filter=ase&sortColumn=Lng')
        assert r is not None
        assert r.status_int == 200
        assert r.content_type == 'application/json'
        assert r.json == answer

    ############################################
    #
    # TESTING POST /players/upload
    #
    ############################################
    
    def test_upload_players_assert_invalid_body(self):
        Player.objects().delete()
        r = self.w.post_json('/players/upload', [
                {
                    "1st": 0,
                    "1st%": 0.0,
                    "20+": 0,
                    "40+": 0,
                    "Att": 1,
                    "Att/G": 0.1,
                    "Avg": 0.0,
                    "FUM": 1,
                    "Lng": "0",
                    "Player": "Drew Kaser",
                    "Pos": "P",
                    "TD": 0,
                    "Team": "SD",
                    "Yds": 0,
                    "Yds/G": 0.0
                },
                {
                    "1st": 7,
                    "1st%": 35.0,
                    "20+": 0,
                    "40+": 0,
                    "Att/G": 2.0,
                    "Avg": 2.6,
                    "FUM": 0,
                    "Lng": "13",
                    "Player": "Case Keenum",
                    "Pos": "QB",
                    "TD": 1,
                    "Team": "LA",
                    "Yds": 51,
                    "Yds/G": 5.1
                }
            ], expect_errors = True)
        assert r is not None
        assert r.status_int == 400
        assert r.content_type == 'application/json'
        assert r.json == { 'arrayIndex': 1, 'errorVariable': 'Att' }

    
    def test_upload_players_success(self):
        Player.objects().delete()
        r1 = self.w.post_json('/players/upload', [
            {
                "Player":"Joe Banyard",
                "Team":"JAX",
                "Pos":"RB",
                "Att":2,
                "Att/G":2,
                "Yds":7,
                "Avg":3.5,
                "Yds/G":7,
                "TD":0,
                "Lng":"7",
                "1st":0,
                "1st%":0,
                "20+":0,
                "40+":0,
                "FUM":0
            },
            {
                "Player":"Shaun Hill",
                "Team":"MIN",
                "Pos":"QB",
                "Att":5,
                "Att/G":1.7,
                "Yds":5,
                "Avg":1,
                "Yds/G":1.7,
                "TD":0,
                "Lng":"9T",
                "1st":0,
                "1st%":0,
                "20+":0,
                "40+":0,
                "FUM":0
            }
        ])
        assert r1 is not None
        assert r1.status_int == 200
        assert r1.text == ''
        
        players = loads(dumps(Player.objects().aggregate([ { '$project': { '_id': 0 }}])))
        assert players == [
            {
                "Player":"Joe Banyard",
                "Team":"JAX",
                "Pos":"RB",
                "Att":2,
                "Att/G":2,
                "Yds":7,
                "Avg":3.5,
                "Yds/G":7,
                "TD":0,
                "Lng":7,
                "LngT":False,
                "1st":0,
                "1st%":0,
                "20+":0,
                "40+":0,
                "FUM":0
            },
            {
                "Player":"Shaun Hill",
                "Team":"MIN",
                "Pos":"QB",
                "Att":5,
                "Att/G":1.7,
                "Yds":5,
                "Avg":1,
                "Yds/G":1.7,
                "TD":0,
                "Lng":9,
                "LngT":True,
                "1st":0,
                "1st%":0,
                "20+":0,
                "40+":0,
                "FUM":0
            }
        ]
