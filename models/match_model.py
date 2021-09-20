# match_model.py
# Created Aug 27, 2021 at 10:52 CEST
# Last updated Sep 17, 2021 at 17:00 CEST

# Standard imports

# Third-party imports
from tinydb import TinyDB

# Local imports

# Other imports

db = TinyDB('database/bracketify.json')
db_matches = db.table('Matches')


class Match:
    """Represents a match
    """

    def __init__(self, p_one, p_two, p_one_score=None, p_two_score=None):
        """Constructor

        - Args:
        p_one & p_two -> str
            Represents a Player instance (participant)
        p_one_score & p_two_score -> int
            Initialize with None and represents the score of a match.
        """

        self.p_one = p_one
        self.p_two = p_two
        self.p_one_score = p_one_score
        self.p_two_score = p_two_score
        self.match_tuple = ()

    """Methods used in Match Class

    - Methods :
        match_results(self, winner):
            Method is used to determine who is the winner
            and add scores to p_on_score & p_two_score
        create_match_tuple(self):
            create match tuples with data
        __str__(self):
            Method is used to cast infos of match into a str.
    """

    def serialize_match(self):
        return {
            'p_one': self.p_one,
            'p_two': self.p_two,
            'p_one_score': self.p_one_score,
            'p_two_score': self.p_two_score
        }

    def create_match(self):
        serialized_match = self.serialize_match()
        test = db_matches.insert(serialized_match)
        return test

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
    def update_scores(cls, score_p1, score_p2, match_id):
        db_matches.update({'p_one_score': score_p1},
                          doc_ids=[match_id])
        db_matches.update({'p_two_score': score_p2},
                          doc_ids=[match_id])

    def create_match_tuple(self):
        self.match_tuple = ([self.p_one, self.p_one_score],
                            [self.p_two, self.p_two_score])
        return self.match_tuple

    @classmethod
    def deserialize_matches(cls, data):
        p_one = data['p_one']
        p_two = data['p_two']
        p_one_score = data['p_one_score']
        p_two_score = data['p_two_score']
        return Match(p_one, p_two, p_one_score, p_two_score)

    @classmethod
    def load_matches_db(cls):
        matches_list = []
        for match in db_matches.all():
            matches_list.append(match)
        return matches_list

    @classmethod
    def get_matches_w_doc_id(cls, doc_id):
        match = db_matches.get(doc_id=doc_id)
        return match

    @classmethod
    def mm_first_round(cls, middle_index, first_half, second_half):

        print("Generating matches for the first round")
        matches_list = []
        for i in range(middle_index):
            match = Match(first_half[i],
                          second_half[i])
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

    def __str__(self):
        return('P1: {} ({}) VS P2: {} ({})').format(self.p_one,
                                                    self.p_one_score,
                                                    self.p_two,
                                                    self.p_two_score)
