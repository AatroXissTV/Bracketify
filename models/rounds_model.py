# rounds_model.py
# Created Aug 27, 2021 at 10:10 CEST
# Last updated Sep 16, 2021 at 10:30 CEST

# Standard imports
from datetime import datetime as d


# Third-party imports
from tinydb import TinyDB

# Local imports
from models.match_model import Match

# Other imports
db = TinyDB('database/bracketify.json')
db_rounds = db.table('Rounds')


class Round:
    """Represents a round.
    """

    def __init__(self, name, round_number, matches_list=[],
                 start_time="", end_time=""):
        """Constructor

        - Args :
            name -> str
                Name of the round in tournament
            matches_list -> list
                List of oll matchs in the round.
            start_time -> str
                Start time of the round.
            end_time -> str
                End time of the round.
        """
        self.name = name
        self.round_number = round_number
        self.matches_list = matches_list
        self.start_time = start_time
        self.end_time = end_time

        """ Methods used in Round model.

        - Methods :
            serialize_round(self):
                Method used to cast round in str
                Return a dict() with round infos.
            round_name(self):
                is used to associate "round" + round_number
            start_round(self):
                Method is used to get the round start date.
            end_round(self):
                Method is used to get the date of the round's end.
            add_matches_to_list(self, match: Match)

        - ClassMethods(cls, data)
            deserialize_round():
                Method used to restore round infos.
        """

    def serialize_round(self):
        return {
            'name': self.name,
            'round_number': self.round_number,
            'matches_list': self.matches_list,
            'start time': self.start_time,
            'end time': self.end_time,
        }

    def create_round(self):
        serialized_round = self.serialize_round()
        round_doc_id = db_rounds.insert(serialized_round)
        return round_doc_id

    @classmethod
    def round_name(cls, round_name):
        name = "Round {}".format(round_name)
        return name

    @classmethod
    def load_round_db(cls):
        rounds_list = []
        for round in db_rounds.all():
            rounds_list.append(round)
        return rounds_list

    @classmethod
    def get_round_with_doc_id(cls, doc_id):
        round = db_rounds.get(doc_id=doc_id)
        return round

    @classmethod
    def mm_first_round(cls, middle_index, first_half, second_half):

        print("Generating matches for the first round")
        matches_list = []

        for i in range(middle_index):
            match = Match(first_half[i]['first_name'],
                          second_half[i]['first_name'])
            print(match)
            serialize_match = match.serialize_match()
            matches_list.append(serialize_match)
        return matches_list

    @classmethod
    def middle_index_players_list(cls, players_in_round):
        length = len(players_in_round)
        middle_index = length//2
        return middle_index

    @classmethod
    def split_first_half(cls, players_in_round, middle_index):
        first_half = players_in_round[:middle_index]
        return first_half

    @classmethod
    def split_second_half(cls, players_in_round, middle_index):
        second_half = players_in_round[middle_index:]
        return second_half

    @classmethod
    def start_round(cls):
        start_time = d.now().strftime("%d/%m/%Y, %H:%M:%S")
        return start_time

    @classmethod
    def end_round(cls):
        end_time = d.now().strftime("%d/%m/%Y, %H:%M:%S")
        return end_time

    @classmethod
    def deserialize_round(cls, data):
        name = data['name']
        round_number = data['round_number']
        match_list = data['matches_list']
        start_time = data['start time']
        end_time = data['end time']
        return Round(name, round_number, match_list, start_time, end_time)
