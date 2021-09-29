# models/round_models.py
# created 22/09/2021 @ 21:47 CEST
# last updated 22/09/2021 @ 21:47 CEST

""" models/round_models.py

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
from datetime import datetime as d

# third-party imports
from tinydb import TinyDB

# local imports

# other
db = TinyDB('database/db_bracketify.json')
db_rounds = db.table('rounds')


class Round:
    """This class represents a round in Bracketify.
    """

    def __init__(self, name, round_number,
                 matches_list=[], start_time="",
                 end_time=""):
        """Constructor

        - Args:
            name -> str
            round_number -> int
            matches_list -> list
            start_time -> str
            end_time -> str
        """

        self.name = name
        self.round_number = int(round_number)
        self.matches_list = matches_list
        self.start_time = start_time
        self.end_time = end_time

    """Summary of methods and quick explanation

    - Methods:
        serialize_round(self):
            used to cast round in str or int type
            return a dict() of these informations

        create_round(self):
            used to insert a new round in 'rounds' DB.

    - ClassMethods
        determine_round_type(cls, len_rl):
            used to determine round type of the tournament.

        time_round():
        method is used to automatically get a date.

        round_name():
            used to set name with current round

        deserialize_round(cls, data):
            used to restore data from JSON objectes
            into Python objects

    __str__ -> cast informations
    """

    def serialize_round(self):
        return {
            'name': self.name,
            'round_number': self.round_number,
            'matches_list': self.matches_list,
            'start_time': self.start_time,
            'end_time': self.end_time
        }

    def create_round(self):
        serialized_round = self.serialize_round()
        round_docid = db_rounds.insert(serialized_round)
        return round_docid

    @classmethod
    def determine_round_type(cls, len_rl):
        if len_rl == 0:
            round = "first_round"
        else:
            round = "round"
        return round

    @classmethod
    def time_round(cls):
        time = d.now().strftime("%d/%m/%Y, %H:%M:%S")
        return time

    @classmethod
    def round_name(cls, current_round):
        round_name = "Round {}".format(current_round)
        return round_name

    @classmethod
    def get_round_with_doc_id(cls, doc_id):
        round = db_rounds.get(doc_id=doc_id)
        return round

    @classmethod
    def update_end_round(cls, end_time, r_doc_id):
        db_rounds.update({'end_time': end_time},
                         doc_ids=[r_doc_id])

    @classmethod
    def deserialize_round(cls, data):
        name = data['name']
        round_number = data['round_number']
        match_list = data['matches_list']
        start_time = data['start_time']
        end_time = data['end_time']
        return Round(name, round_number, match_list,
                     start_time, end_time)

    def __str__(self) -> str:
        return ("Name: {}\nStarted @ {}\nEnded@ {}\n"
                .format(self.name, self.start_time,
                        self.end_time))
