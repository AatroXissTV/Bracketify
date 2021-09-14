# player_model.py
# Created Aug 26, 2021 at 12:00 CEST
# Last Updated Sep 10, 2021 at 15:12

# Standard imports

# Third-party imports
from tinydb import TinyDB
from tinydb.queries import where

# Local imports

# Other imports

# Create or Open DB
db = TinyDB('database/bracketify.json')
db_players = db.table('players')


class Player:
    """ Represents a player
    """

    def __init__(self, name, first_name, birth_date, gender, rank=0):
        """Constructor

        - Args:
            name -> str
                Name of the player.
            first_name -> str
                First name of the player.
            birth_date -> str
                Birthday of the player.
            gender -> str
                Gender of the player.
            rank -> int
                Current rank of the player.
                Must be a positive int.
        """

        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = int(rank)

    """Methods used in Player class

    - Methods:
        serialize_player(self):
            Method used to cast player infos in str or int type.
            Return a dict() of these infos.
        create_player(self):
            Method used to create a new player in 'players' DB.
        update_player_rank(self, player_id, new_rank)
            Method used to update player rank in 'players' DB.
            player_id -> int
                is the player's ID in 'players' DB.
            new_rank -> int
                is the new rank user wants ton insert in 'players' DB.

    - ClassMethods : (don't require creation of a class instance)
        deserialize_player(cls, data)
            Method is used to restore data from JSON objects
            in 'players' DB into a Python object.
        load_players_db(cls)
            Method is used to cast JSON objects in 'players' DB
            into a list.
        get_players_ordered_by_rank(cls, players_list)
            Method is used to cast JSON objects in 'players' DB
            into a list.
            Then JSON objects are sorted by 'rank'
        get_players_ordered_by_name(cls, players_list)
            Method is used to cas JSON objects in 'players' DB
            into a list.
            Then JSON objects are sorted  by 'name'.
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
        db_players.insert(serialized_player)

    def update_player_rank(self, new_rank, player_id):
        db_players.update({'rank': new_rank}, doc_ids=[player_id])

    @classmethod
    def deserialize_player(cls, data):
        name = data['name']
        first_name = data['first_name']
        birth_date = data['birth_date']
        gender = data['gender']
        rank = data['rank']
        return Player(name, first_name, birth_date, gender, rank)

    @classmethod
    def load_players_db(cls):
        players_list = []
        for player in db_players.all():
            players_list.append(player)
        return players_list

    @classmethod
    def get_player_doc_id(cls, name):
        for player in db_players.search(where('name') == name):
            player_doc_id = player.doc_id
            return player_doc_id

    @classmethod
    def get_player_with_doc_id(cls, doc_id):
        player = db_players.get(doc_id=doc_id)
        return player

    @classmethod
    def get_players_ordered_by_rank(cls, players_list):
        players_list.sort(key=lambda x: x['rank'])
        return players_list

    @classmethod
    def get_players_ordered_by_name(cls, players_list):
        players_list.sort(key=lambda x: x['name'])
        return players_list

    def __str__(self):
        return ('Player: {} {} (Rank {})\nBirth date: {}\nGender: {}\n'
                .format(self.first_name, self.name, self.rank,
                        self.birth_date, self.gender))
