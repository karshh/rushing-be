import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import unittest
import json
from mongoengine import connect, disconnect
from database.player import Player
from services import player_service
from datetime import datetime
from settings import TEST_MONGO_URL
from tests.constants import PLAYERS_RAW_DATA

class TestPlayersService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        disconnect()
        connect('mongoenginetest', host=TEST_MONGO_URL)
        Player.objects().delete()

    @classmethod
    def tearDownClass(cls):
       disconnect()

    ############################################
    #
    # TESTING player_service.get_players
    #
    ############################################

    def test_get_players_assert_sortColumn_not_none(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', None, '1', None, None)
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_SORT_COLUMN'
        except:
            assert False

    def test_get_players_assert_sortColumn_not_valid(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', 'invalid', '1', None, None)
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_SORT_COLUMN'
        except:
            assert False

    def test_get_players_assert_sortDirection_not_none(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', 'Player', None, None, None)
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_SORT_DIRECTION'
        except:
            assert False

    def test_get_players_assert_sortDirection_not_valid(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', 'Player', 'invalid', None, None)
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_SORT_DIRECTION'
        except:
            assert False

    def test_get_players_assert_skip_not_valid(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', 'Player', '1', 'invalid', None)
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_SKIP'
        except:
            assert False

    def test_get_players_assert_limit_not_valid(self):
        Player.objects().delete()
        try:
            result = player_service.get_players('As', 'Player', '1', None, 'invalid')
            assert False
        except ValueError as e:
            assert str(e) == 'INVALID_LIMIT'
        except:
            assert False
    
    def test_get_players_test_empty_data(self):
        Player.objects().delete()
        answer = {
            'size': 0,
            'players': []
        }
        result = player_service.get_players('', 'Player', '1', None, None)
        assert result == answer
        

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
        result = player_service.get_players('', 'Player', '1', None, None)
        assert result == answer

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
        result = player_service.get_players('', 'Player', '-1', None, None)
        assert result == answer

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
        result = player_service.get_players('', 'Lng', '1', None, None)
        assert result == answer

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
        result = player_service.get_players('', 'Lng', '1', 5, None)
        assert result == answer

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
        result = player_service.get_players('', 'Lng', '1', 5, 2)
        assert result == answer


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
        result = player_service.get_players('ase', 'Lng', '1', None, None)
        assert result == answer
