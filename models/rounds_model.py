# rounds_model.py
# Created Aug 27, 2021 at 10:10 CEST
# Last updated Sep 01, 2021 at 10:21 CEST

# Standard imports
from datetime import datetime as d

# Third-party imports

# Local imports

# Other imports


class Round:
    """Represents a round of a tournament.
    """

    def __init__(self, name, round_number, matches_list=[],
                 start_time="", end_time=""):
        """Constructor

        - Args :
            name -> str
                Name of the round in tournament
            match_list -> list
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

    def round_name(self):
        self.name = "Round {}".format(self.round_number)
        return self.name

    def start_round(self):
        self.start_time = d.now().strftime("%d/%m/%Y, %H:%M:%S")
        return self.start_time

    def end_round(self):
        self.end_time = d.now().strftime("%d/%m/%Y, %H:%M:%S")

    @classmethod
    def deserialize_round(cls, data):
        name = data['name']
        round_number = data['round_number']
        match_list = data['matches_list']
        start_time = data['start time']
        end_time = data['end time']
        return Round(name, round_number, match_list, start_time, end_time)


"""TEST ROUND MODEL
"""
round1 = Round("Round", "1", ["Adrien (None) VS Xavier (None)",
               "Marianne (None) VS Colas (None)"])
serialized = round1.serialize_round()
print(serialized)
print("----------------------")

name_round = round1.round_name()
serialized2 = round1.serialize_round()
print(serialized2)
print("----------------------")

start_round = round1.start_round()
serialized3 = round1.serialize_round()
print(serialized3)
