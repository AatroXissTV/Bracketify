# participant_model.py
# Created Aug 31, 2021 at 15:00 CEST
# Last updated Sep 06, 2021 at 09:53 CEST

# Standard imports

# Third-party imports

# Local imports

# Other imports


class Participant:
    """Represents a participant in the tournament
    """

    def __init__(self, player_id, player_firstname, player_lastname,
                 round_score=0, tournament_score=0, p=""):
        """Constructor

        - Args:
            player_id -> int
                This attribute is used to set the player ID stored in the DB
                as participant in the tournament.
            p -> str
            Represents the player firstname and lastname joined
            player_firstname -> str
                This is the player firstname.
            player_lastname -> str
                This the player lastname
            round_score -> int
                Is used to set the score of a participant in the tournament
            tournament_score -> int
                Is used to set final score of a participant in the tournament
        """

        self.player_id = player_id
        self.p = p
        self.player_firstname = player_firstname
        self.player_lastname = player_lastname
        self.round_score = round_score
        self.tournament_score = tournament_score

    """Methods used in Participant Class

    - Methods:
        serialize_participant(self):
            Method is used to cast a participant infos in str or int type.
            Return a dict() with this infos.
        join_first_name_and_lastname(self):
            Method is used to join player first name and last name
            so it can be casted in matches.
    """

    def serialize_participant(self):
        return {
            'player_id': self.player_id,
            'p': self.p,
            'player_firstname': self.player_firstname,
            'player_lastname': self.player_lastname,
            'round_score': self.round_score,
            'tournament_score': self.tournament_score
        }

    def join_firstame_and_lastname(self):
        self.p = self.player_firstname + " " + self.player_lastname
        return self.p
