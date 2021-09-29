# models/tournament_models.py
# created 22/09/2021 @ 21:32 CEST
# last updated 22/09/2021 @ 21:32 CEST

""" models/tournament_models.py

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
from models.match_models import Match
from tinydb import TinyDB

# local imports
from models.round_models import Round

# other
db = TinyDB('database/db_bracketify.json')
db_tournaments = db.table('tournaments')


class Tournament:
    """This class represents a tournament in Bracketify.
    """

    def __init__(self, name, location, start_date, end_date,
                 description, rules, rounds_number,
                 players_list=[], rounds_list=[]):
        """Constructor

        - Args:
            name -> str
            location -> str
            start_date -> str
            end_date -> str
            description -> str
            rules -> str
            rounds_number -> int
            players_list -> list()
            rounds_list -> list()
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

    """Summary of methods and quick explanation

    - Methods:
        serialize_tournament(self):
            used to cast tournament informations in str or int type
            return a dict() of these informations

        create_tournament(self):
            used to create a new tournament in 'tournaments' DB
            return tournament_id

        update_rounds_list(self, new_list, t_docid):
            update rounds_list in tournaments DB.

    - ClassMethods:
        load_tournament_docid_db(cls):
            used to retrieve tournaments doc_id in DB.

        get_tournament_w_docid(cls, docid):
            used to retrieve a tournament information
            with the tournament doc_ID

        get_len_rounds_list(cls, tournament_id):
            used to get length rounds_list
            with the tournament doc_IC

        deserialize_tournament(cls,data):
            used to restore data from JSON objectes
            into Python objects

    __str__ -> cast informations
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
            'rounds_list': self.rounds_list
        }

    def create_tournament(self):
        serialized_tournament = self.serialize_tournament()
        tournament_id = db_tournaments.insert(serialized_tournament)
        return tournament_id

    def update_rounds_list(self, new_list, t_docid):
        db_tournaments.update({'rounds_list': new_list}, doc_ids=[t_docid])

    def check_if_p_were_opponents(self, tournament_docid, p1, p2):
        tournament = Tournament.get_tournament_w_docid(tournament_docid)
        matches_list = []
        for round_docid in tournament['rounds_list']:
            round = Round.get_round_with_doc_id(round_docid)
            for match_docid in round['matches_list']:
                matches_list.append(match_docid)

        for match_docid in matches_list:
            match = Match.get_matches_w_doc_id(match_docid)
            m_p1 = match['p_one']
            m_p2 = match['p_two']

            if p1 == m_p1 and p2 == m_p2:
                value = True
                break
            else:
                if p2 == m_p1 and p1 == m_p2:
                    value = True
                    break
                else:
                    value = False
        return value

    @classmethod
    def load_tournament_docid_db(cls):
        tournament_docid_list = []
        for tournament in db_tournaments.all():
            tournament_docid_list.append(tournament.doc_id)
        return tournament_docid_list

    @classmethod
    def get_tournament_w_docid(cls, doc_id):
        tournament = db_tournaments.get(doc_id=doc_id)
        return tournament

    @classmethod
    def get_len_rounds_list(cls, tournament_id):
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        len_rounds_list = len(tournament['rounds_list'])
        return len_rounds_list

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
        return Tournament(name, location, start_date,
                          end_date, description,
                          rules, rounds_number,
                          players_list)

    def __str__(self) -> str:
        return ("Name: {}\nLocation: {}\nDate {} - {}\nRounds Number: {}\n"
                "Rules: {}\nDescription: {}\n".format(self.name, self.location,
                                                      self.start_date,
                                                      self.end_date,
                                                      self.rounds_number,
                                                      self.rules,
                                                      self.description))
