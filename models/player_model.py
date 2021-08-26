# player_model.py

# Standard imports

# Third-party imports
from tinydb import TinyDB

# Local imports

# Other imports

# TinyDB
db = TinyDB('database/bracketify.json')
db_players = db.table('players')


class Player:
    """Represents a player
    """

    def __init__(self, name,
                 first_name, birth_date, gender, rank=0):
        """Summary of __init__

        -Args:
            name : str
                Name of the player.
            first_name : str
                Firstname of the player.
            birth_date : str
                Birthday of the player.
            gender : str
                Gender of the plater.
            rank : int
                Player rank.
        """
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = int(rank)

        """Summary of methods used in Player Class

        - Methods :
            serialize_player():
                Method used to cast player informations in str or int type.
                Return a dict() of these informations
            deserialize_player():
                Methode used to restore player informations

            insert_player():
                Method is used to insert a new player in the 'players' DB.

            __str__():
                Method is used to debug & tests purposes.
        """

    def serialize_player(self):
        return {
            'name': self.name,
            'firstname': self.first_name,
            'birthdate': self.birth_date,
            'gender': self.gender,
            'rank': self.rank
        }

    def deserialize_player(self, serialized_player):
        self.name = serialized_player['name']
        self.first_name = serialized_player['firstname']
        self.birth_date = serialized_player['birthdate']
        self.gender = serialized_player['gender']
        self.rank = serialized_player['rank']

    def insert_player(self):
        db_players.insert(self.serialize_player())

    def __str__(self) -> str:
        return ('Player : {} {}\nBirth Date : {}\nGender : {}\nRank : {}\n'
                .format(self.name, self.first_name, self.birth_date,
                        self.gender, self.rank))


"""TEST PLAYER MODEL
Creating 3 players in DB.
"""
player1 = Player(name='Nougaret', first_name='Adrien', birth_date='01/03/1990',
                 gender='M', rank='1')
player2 = Player(name='Dang', first_name='Xavier', birth_date='26/08/1980',
                 gender='M', rank='3')
player3 = Player(name='LBW', first_name='Marianne', birth_date='13/11/1994',
                 gender='F', rank='2')

serialized = player1.serialize_player()
player1.insert_player()
player1.deserialize_player(serialized)
print(str(player1))

serialized = player2.serialize_player()
player2.insert_player()
player2.deserialize_player(serialized)
print(str(player2))

serialized = player3.serialize_player()
player3.insert_player()
player3.deserialize_player(serialized)
print(str(player3))
