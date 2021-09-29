# models/match_models.py
# created 22/09/2021 @ 21:58 CEST
# last updated 22/09/2021 @ 21:58 CEST

""" models/match_models.py

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
from tinydb import TinyDB

# local imports

# other
db = TinyDB('database/db_bracketify.json')
db_matches = db.table('matches')


class Match:
    """This class represents a match in Bracketify
    """

    def __init__(self, p_one, p_two,
                 p_one_score=None, p_two_score=None,
                 p_one_points=0, p_two_points=0):
        """Constructor

        -Args:
            p_one -> int
            p_two -> int
            p_one_score -> int
            p_two_score -> int
        """

        self.p_one = p_one
        self.p_two = p_two
        self.p_one_score = p_one_score
        self.p_two_score = p_two_score
        self.p_one_points = p_one_points
        self.p_two_points = p_two_points
        self.match_tuple = ()

    """Summary of methods and quick explanation

    - Methods :
        serialize_match(self):
            used to cast round in str or int type
            return a dict() of these informations

        create_match(self):
            used to insert a new match in 'matches' DB.
            Return a docid of the newly created match

    - ClassMethods:
        middle_index_list(cls, ordered_docid):
            used to determine the middle of a list

        first_half_list(cls, ordered_docid, middle_index):
            used to get first half of a list

        second_half_list(cls, ordered_docid, middle_index):
            used to get second half of a list

        set_matches_first_r(cls, middle_index, first_half, second_half):
            this method is used to do the pairing of players
            for the first round of a tournament.

        deserialize_match(cls, data):
            used to restore data from JSON objectes
            into Python objects

    __str__ -> cast infromations
    """

    def serialize_match(self):
        return {
            'p_one': self.p_one,
            'p_two': self.p_two,
            'p_one_score': self.p_one_score,
            'p_two_score': self.p_two_score,
            'p_one_points': self.p_one_points,
            'p_two_points': self.p_two_points
        }

    def create_match(self):
        serialized_match = self.serialize_match()
        match_doc_id = db_matches.insert(serialized_match)
        return match_doc_id

    def create_match_tuple(self):
        self.match_tuple = ([self.p_one, self.p_one_points],
                            [self.p_two, self.p_two_points])
        return self.match_tuple

    def match_results(self, winner):
        if winner == "0":
            self.p_one_score = 0.5
            self.p_two_score = 0.5
        elif winner == "1":
            self.p_one_score = 1
            self.p_two_score = 0
        elif winner == "2":
            self.p_one_score = 0
            self.p_two_score = 1

    @classmethod
    def middle_index_list(cls, ordered_docid):
        length = len(ordered_docid)
        middle_index = length//2
        return middle_index

    @classmethod
    def first_half_list(cls, ordered_docid, middle_index):
        first_half = ordered_docid[:middle_index]
        return first_half

    @classmethod
    def second_half_list(cls, ordered_docid, middle_index):
        second_half = ordered_docid[middle_index:]
        return second_half

    @classmethod
    def set_matches_first_r(cls, middle_index, firs_half, second_half):
        matches_list = []
        for i in range(middle_index):
            match = Match(firs_half[i],
                          second_half[i])
            serialize_match = match.serialize_match()
            matches_list.append(serialize_match)
        return matches_list

    @classmethod
    def get_matches_w_doc_id(cls, doc_id):
        match = db_matches.get(doc_id=doc_id)
        return match

    @classmethod
    def update_scores(cls, score_p1, score_p2, match_id):
        db_matches.update({'p_one_score': score_p1},
                          doc_ids=[match_id])
        db_matches.update({'p_two_score': score_p2},
                          doc_ids=[match_id])

    @classmethod
    def update_points(cls, points_p1, points_p2, match_id):
        db_matches.update({'p_one_points': points_p1},
                          doc_ids=[match_id])
        db_matches.update({'p_two_points': points_p2},
                          doc_ids=[match_id])

    @classmethod
    def deserialize_matches(cls, data):
        p_one = data['p_one']
        p_two = data['p_two']
        p_one_score = data['p_one_score']
        p_two_score = data['p_two_score']
        p_one_points = data['p_one_points']
        p_two_points = data['p_two_points']
        return Match(p_one, p_two, p_one_score, p_two_score,
                     p_one_points, p_two_points)

    def __str__(self):
        return('P1: {} ({}) VS P2: {} ({})').format(self.p_one,
                                                    self.p_one_score,
                                                    self.p_two,
                                                    self.p_two_score)
