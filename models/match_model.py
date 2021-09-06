# match_model.py
# Created Aug 27, 2021 at 10:52 CEST
# Last updated Sep 06, 2021 at 10:15 CEST

# Standard imports

# Third-party imports

# Local imports

# Other imports

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
            Method is used to cas infos of match into a str.
    """

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

    def create_match_tuple(self):
        self.match_tuple = ([self.p_one, self.p_one_score],
                            [self.p_two, self.p_two_score])
        return self.match_tuple

    def __str__(self):
        return('{} ({}) VS {} ({})').format(self.p_one,
                                            self.p_one_score,
                                            self.p_two,
                                            self.p_two_score)
