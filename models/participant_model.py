# participant_model.py
# Created Aug 31, 2021 at 15:00 CEST
# Last updated Aug 31, 2021 at 15:00 CEST

# Standard imports

# Third-party imports

# Local imports

# Other imports


class Participant:
    """Represents a participant in the tournament
    """

    def __init__(self, player_id, round_score=0, tournament_score=0):
        """Constructor

        - Args:
            player_id -> int
                This attribute is used to set the player ID stored in the DB
                as participant in the tournament.
            round_score -> int
                Is used to set the score of a participant in the tournament
            tournament_score -> int
                Is used to set final score of a participant in the tournament
        """

        self.player_id = player_id
        self.round_score = round_score
        self.tournament_score = tournament_score

    """Methods used in Participant Class

    - Methods:
        serialize_participant(self):
            Method is used to cast a participant infos in str or int type.
            Return a dict() with this infos.
    """

    def serialize_participant(self):
        return {
            'player_id': self.player_id,
            'round_score': self.round_score,
            'tournament_score': self.tournament_score
        }
