# models/player_models.py
# created 22/09/2021 @ 21:11 CEST
# last updated 27/09/2021 @ 09:33 CEST

""" models/player_models.py

To do:
    * Update Requirements with TinyDB.
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports

# third-party imports
from tinydb import TinyDB, where

# local imports

# other
db = TinyDB('database/db_bracketify.json')
db_players = db.table('players')


class Player:
    """This class represents an Actor in Bracketify.
    """

    def __init__(self, name, first_name, birth_date, gender, rank=0):
        """Constructor

        - Args:
            name -> str
            first_name -> str
            birth_date -> str
            gender -> str
            rank -> int
        """

        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = int(rank)

    """Summary of Methods and quick explanation

    - Methods:
        serialize_player(self):
            used to cast player informations in str or int type
            return a dict() of these informations.

        create_player(self):
            used to create a new player in 'players' DB.
            return player_id

        update_player_rank(self, new_rank, player_docid):
            used to update a player rank in DB with player doc_ID

    - ClassMethods (don't require creation of class instance)
        load_players_docid_db(cls):
            used to retrieve players doc_ID in DB.

        get_player_w_docid(cls, doc_id):
            used to retrieve a player informations
            with player doc_ID

        get_player_docid(cls, player):
            used to retrieve a player id
            From JSON str

        from_id_list_order_players_by_rank(cls, players_docid_list):
            used to sort players from id list into JSON list
            with players ordered by rank

        get_players_ordered_by_name(cls, players_list, reverse_a):
            used to sort players_list by name
            reverse is either True or False

        get_players_ordered_by_rank(cls, players_list, reverse_a):
            used to sort players_list by rank
            reverse is either True or False

        deserialize_player(cls, data):
            used to restore data from JSON objects
            into Python objects

    __str__ -> cast informations
    """

    def serialize_player(self):
        return {
            'name': self.name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'rank': self.rank
        }

    def create_player(self):
        serialized_player = self.serialize_player()
        player_id = db_players.insert(serialized_player)
        return player_id

    def update_player_rank(self, new_rank, player_docid):
        db_players.update({'rank': new_rank}, doc_ids=[player_docid])

    @classmethod
    def load_players_docid_db(cls):
        players_docid_list = []
        for player in db_players.all():
            players_docid_list.append(player.doc_id)
        return players_docid_list

    @classmethod
    def get_player_w_docid(cls, doc_id):
        player = db_players.get(doc_id=doc_id)
        return player

    @classmethod
    def get_player_docid(cls, player):
        for player in db_players.search(where('rank') == player['rank']):
            player_doc_id = player.doc_id
            return player_doc_id

    @classmethod
    def from_id_list_order_players_by_rank(cls, players_docid_list):
        players_list = []
        for p_docid in players_docid_list:
            player = Player.get_player_w_docid(p_docid)
            players_list.append(player)
        ordered_p = Player.get_players_ordered_by_rank(players_list,
                                                       False)
        return ordered_p

    @classmethod
    def get_players_ordered_by_name(cls, players_list, reverse_a):
        players_list.sort(key=lambda x: x['name'], reverse=reverse_a)
        return players_list

    @classmethod
    def get_players_ordered_by_rank(cls, players_list, reverse_a):
        players_list.sort(key=lambda x: x['rank'], reverse=reverse_a)
        return players_list

    @classmethod
    def deserialize_player(cls, data):
        name = data['name']
        first_name = data['first_name']
        birth_date = data['birth_date']
        gender = data['gender']
        rank = data['rank']
        return Player(name, first_name, birth_date, gender, rank)

    def __str__(self) -> str:
        return ('Player: {} {} (Rank {})\nBirthdate {} - {}\n'
                .format(self.name, self.first_name,
                        self.rank, self.birth_date,
                        self.gender))
