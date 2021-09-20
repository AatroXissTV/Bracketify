# tournament_model.py
# Created Aug 26, 2021 at 12:13 CEST
# Last Updated Sep 20, 2021 at 17:00

# Standard imports

# Third-party imports
from tinydb import TinyDB
from tinydb.queries import where

# Local imports
from models.player_model import Player

# Other imports

# Create or Open DB.
db = TinyDB('database/bracketify.json')
db_tournaments = db.table('tournaments')


class Tournament:
    """Represents a tournament
    """

    def __init__(self, name, location, start_date, end_date, description,
                 rules, rounds_number, players_list=[], rounds_list=[]):
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
        self.rounds_number = rounds_number
        self.players_list = players_list
        self.rounds_list = rounds_list

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
            'rounds_number': self.rounds_number,
            'players_list': self.players_list,
            'rounds_list': self.rounds_list,
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
        rounds_number = data['rounds_number']
        players_list = data['players_list']
        return Tournament(name, location, start_date, end_date, description,
                          rules, rounds_number, players_list)

    @classmethod
    def load_tournaments_db(cls):
        tournaments_list = []
        for tournament in db_tournaments.all():
            tournaments_list.append(tournament)
        return tournaments_list

    @classmethod
    def get_tournament_doc_id(cls, name):
        for tournament in db_tournaments.search(where('name') == name):
            tournament_doc_id = tournament.doc_id
            return tournament_doc_id

    @classmethod
    def get_tournament_with_doc_id(cls, doc_id):
        tournament = db_tournaments.get(doc_id=doc_id)
        return tournament

    @classmethod
    def get_players_in_t(cls, tournament_id):
        t = Tournament.get_tournament_with_doc_id(tournament_id)
        players_docid = t['players_list']
        players_list = []
        for doc_id in players_docid:
            player = Player.get_player_with_doc_id(doc_id)
            players_list.append(player)
        return players_list

    @classmethod
    def update_round_list(cls, tournament_id, r_doc_id):
        db_tournaments.update({'rounds_list': [r_doc_id]},
                              doc_ids=[tournament_id])

    def __str__(self) -> str:
        return ("Name: {}\nLocation: {}\nDate {} - {}\nRounds Number: {}\n"
                "Rules: {}\nDescription: {}\n".format(self.name, self.location,
                                                      self.start_date,
                                                      self.end_date,
                                                      self.rounds_number,
                                                      self.rules,
                                                      self.description))
