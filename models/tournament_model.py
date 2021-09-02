# tournament_model.py
# Created Aug 26, 2021 at 12:13 CEST
# Last updated Aug 31, 2021 at 13:17 CEST

# Standard imports

# Third-party imports
from tinydb import TinyDB

# Local imports

# Other imports

# Create or Open DB.
db = TinyDB('database/bracketify.json')
db_tournaments = db.table('tournaments')

NUMB_OF_ROUNDS = 4


class Tournament:
    """Represents a tournament
    """

    def __init__(self, name, location, start_date, end_date, description,
                 rules, rounds_list=[], players_list=[]):
        """Constructor

        - Args:
            name -> str
                Name of the tournament.
            location -> str
                Location of the tournament.
            start_date & end_date -> str
                Duration of the tournament.
            rules -> str
                Rules of the tournament
                Either blitz, bullet or rapide.
            description -> str
                Description of the tournament.
            rounds_list -> list()
                List of all rounds in the tournament.
            players_list -> dict()
                Dictionnary of all the players participating.
        """

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rules = rules
        self.rounds_list = rounds_list
        self.players_list = players_list

    """Methods used in Tournament class

    - Methods:
        serialize_tournament(self):
            Method used to cas tournaments infos in str or int type.
            Return a dict() with these infos.
        create_tournament(self):
            Method used to create a new tournament in 'tournaments' DB.

    - ClassMethods:
        deserialize_tournament(cls, data):
            Method is used to restore data from JSON objects
            in 'tournaments' DB into a Python object.
        load_tournaments_db(cls):
            Method is used to cast JSON objects in 'tournaments' DB
            into a list
    """
    def serialize_tournament(self):
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'rules': self.rules,
            'rounds_list': self.rounds_list,
            'players_list': self.players_list
        }

    def create_tournament(self):
        serialized_tournament = self.serialize_tournament()
        db_tournaments.insert(serialized_tournament)

    @classmethod
    def deserialize_tournament(cls, data):
        name = data['name']
        location = data['location']
        start_date = data['start_date']
        end_date = data['end_date']
        description = data['description']
        rules = data['rules']
        rounds_list = data['rounds_list']
        players_list = data['players_list']
        return Tournament(name, location, start_date, end_date, description,
                          rules, rounds_list, players_list)

    @classmethod
    def load_tournaments_db(cls):
        tournaments_list = []
        for tournament in db_tournaments.all():
            tournaments_list.append(tournament)
        return tournaments_list


"""TESTING MODEL
"""
# Create tournaments objects
tournament1 = Tournament(name='GamePass Challenge #1', location='Lyon',
                         start_date='1450', end_date='1600', description='txt',
                         rules='blitz', rounds_list=[], players_list=[])
tournament2 = Tournament(name='Fight for sub', location='Montpellier',
                         start_date='1700', end_date='0000', description='txt',
                         rules='rapide', rounds_list=[], players_list=[])
tournament3 = Tournament(name='Zlan', location='Lyon',
                         start_date='1300', end_date='0000', description='txt',
                         rules='blitz', rounds_list=[], players_list=[])

# Serialize + insert Tournament Objects in DB.
serialized = tournament1.serialize_tournament()
tournament1.create_tournament()

serialized = tournament2.serialize_tournament()
tournament2.create_tournament()

serialized = tournament3.serialize_tournament()
tournament3.create_tournament()

# Load DB
load1 = Tournament.load_tournaments_db()
print(load1)
