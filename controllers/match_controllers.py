# controllers/match_controllers.py
# created 24/09/2021 @ 11:27 CEST
# last updated 24/09/2021 @ 11:27 CEST

""" controllers/match_controller.py

To do:
    * insert tasks
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.5.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports
from operator import itemgetter

# third-party imports

# local imports
from models.round_models import Round
from models.match_models import Match
from models.player_models import Player
from models.tournament_models import Tournament
from views.round_views import RoundMenu

# other


class MatchController():
    """this class represents the match controller of Bracketify.
    Summary of methods and quick explanation:

    - Methods :
        sort_players(tournament_id):
            used to order players list with the player ranks.
            return a list with ordered player_IDS.

        matchmaking_first_round(ordered_docid):
            used to do the matchmaking of the first round.
            return a list of the matches.

        create_matches(matchmaking):
            is used to create each matches in list of matches.
            return a list of IDs of matches

        ask_winner(title, match_selected):
            is used to ask the winner of a match and update scores
            in 'matches' DB.

        update_scores(match_selected, i):
            is used to update score in 'matches' DB.

        calculate_points(tournament_id):
            retrieve the previous round and get the last element.
            retrieve points & scores.
            Add scores to points and return points.

    """

    def sort_players(tournament_id):
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        p_docid_list = tournament['players_list']
        ordered_p = Player.from_id_list_order_players_by_rank(p_docid_list)
        ordered_docid = []
        for player in ordered_p:
            doc_id = Player.get_player_docid(player)
            ordered_docid.append(doc_id)
        return ordered_docid

    def matchmaking_first_round(ordered_docid):
        middle_index = Match.middle_index_list(ordered_docid)
        first_half = Match.first_half_list(ordered_docid, middle_index)
        second_half = Match.second_half_list(ordered_docid, middle_index)
        matches_list = Match.set_matches_first_r(middle_index,
                                                 first_half,
                                                 second_half)
        return matches_list

    def create_matches(matchmaking):
        matches_docid_list = []
        for matches in matchmaking:
            deserialized_match = Match.deserialize_matches(matches)
            match_docid = Match.create_match(deserialized_match)
            matches_docid_list.append(match_docid)
        return matches_docid_list

    def ask_winner(title, match_selected):
        menu = RoundMenu(app_title=title)

        ask_winner_menu = menu.ask_winner()

        if (ask_winner_menu == "0"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            MatchController.calculate_points(match_selected)

        elif (ask_winner_menu == "1"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            MatchController.calculate_points(match_selected)

        elif (ask_winner_menu == "2"):
            i = ask_winner_menu
            match = MatchController.update_scores(match_selected,
                                                  i)
            MatchController.calculate_points(match_selected)

        return match

    def update_scores(match_selected, i):
        get_match = Match.get_matches_w_doc_id(match_selected)
        match_object = Match.deserialize_matches(get_match)
        match_object.match_results(i)
        serialized_match = match_object.serialize_match()
        match_object.update_scores(serialized_match['p_one_score'],
                                   serialized_match['p_two_score'],
                                   match_selected)
        get_new_match = Match.get_matches_w_doc_id(match_selected)
        new_match = Match.deserialize_matches(get_new_match)
        return new_match

    def calculate_points(match_selected):
        get_match = Match.get_matches_w_doc_id(match_selected)
        points_p1 = get_match['p_one_score'] + get_match['p_one_points']
        points_p2 = get_match['p_two_score'] + get_match['p_two_points']
        Match.update_points(points_p1, points_p2, match_selected)
        Match.get_matches_w_doc_id(match_selected)

    def get_match_tuples(last_round):
        round = Round.get_round_with_doc_id(last_round)
        matches_list = round['matches_list']
        matches_tuples = []
        for match in matches_list:
            get_match = Match.get_matches_w_doc_id(match)
            deserialized = Match.deserialize_matches(get_match)
            match_tuple = Match.create_match_tuple(deserialized)
            matches_tuples.append(match_tuple)
        return matches_tuples

    def sort_players_round(matches_tuples):
        player_list = []
        for tuple in matches_tuples:
            for player in tuple:
                player_list.append(player)

        for player in player_list:
            get_player = Player.get_player_w_docid(player[0])
            rank = get_player['rank']
            player.append(rank)

        sorted_player = sorted(player_list, key=itemgetter(1, 2), reverse=True)

        return sorted_player

    def matchmaking_round(ordered_list):
        first_half = ordered_list[::2]
        second_half = ordered_list[1:len(ordered_list):2]

        length = len(ordered_list)//2

        matches_list = []
        for i in range(length):
            match = Match(first_half[i][0], second_half[i][0],
                          None, None,
                          first_half[i][1], second_half[i][1],)
            serialize_match = match.serialize_match()
            matches_list.append(serialize_match)

        return matches_list
