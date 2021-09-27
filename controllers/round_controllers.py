# controllers/round_controllers.py
# created 24/09/2021 @ 11:12 CEST
# last updated 24/09/2021 @ 11:12 CEST

""" controllers/round_controller.py

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

# third-party imports

# local imports
from old.cli_view_old import Cli
from models.match_models import Match
from models.player_models import Player
from models.tournament_models import Tournament
from models.round_models import Round
from views.round_views import RoundMenu
from controllers.match_controllers import MatchController

# other


class RoundController():
    """this class represents the round controller of Bracketify
    Summary of methods and quick explanation:

    - Methods :
        rounds_management(tournament_id):
            used to know if the programs needs to create another
            round of the tournament based on 'rounds_number' in
            'tournaments' DB & current length of 'rounds_list'.
            'rounds_list' -> list of rounds IDs in 'tournaments' DB.

        go_next_round(tournament_id, rounds_number, len_rounds_list):
            used to go to next round if its the first round launch first_round
            else launch round.

        first_round(tournament_id, current_round):
            used to manage the pairing & creation of first round

        create_round(matches_docid_list, current_round):
            create round in 'rounds' DB.
    """

    def rounds_management(tournament_id, title):
        round_menu = RoundMenu(app_title=title)
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        rounds_number = tournament['rounds_number']
        len_rounds_list = Tournament.get_len_rounds_list(tournament_id)

        while (len_rounds_list != (rounds_number-1)):
            Cli.cli_entry(title)
            answers = round_menu.start_round()
            if answers['confirm']:
                len_rounds_list = Tournament.get_len_rounds_list(tournament_id)
                print("Numb Round Tournament: {} | Previous round: {}"
                      .format(rounds_number, len_rounds_list))

                current_round = len_rounds_list+1
                RoundController.go_next_round(tournament_id,
                                              current_round,
                                              len_rounds_list, title)
            else:
                break
            # ASK if you want to go to next_round
        else:
            print("Tournoi Terminé !")
            print("Numb Round Tournament: {} | Previous round: {}"
                  .format(rounds_number, len_rounds_list))

    def go_next_round(tournament_id, current_round, len_rounds_list, title):
        round_type = Round.determine_round_type(len_rounds_list)
        if (round_type == "first_round"):
            r_docid = RoundController.first_round(tournament_id, current_round)
            RoundController.update_rounds_list(tournament_id, r_docid)
            RoundController.attribute_results(title, r_docid)

        else:
            last_r_docid = RoundController.get_last_round_docid(tournament_id)
            r_docid = RoundController.round(tournament_id, current_round,
                                            last_r_docid)
            RoundController.update_rounds_list(tournament_id, r_docid)
            RoundController.attribute_results(title, r_docid)

    def first_round(tournament_id, current_round):
        ordered_docid = MatchController.sort_players(tournament_id)
        matchmaking = MatchController.matchmaking_first_round(ordered_docid)
        matches_docid_list = MatchController.create_matches(matchmaking)
        r_docid = RoundController.create_round(matches_docid_list,
                                               current_round)
        return r_docid

    def round(tournament_id, current_round, last_round_docid):
        matches_tuples = MatchController.get_match_tuples(last_round_docid)
        ordered_list = MatchController.sort_players_round(matches_tuples)
        matchmaking = MatchController.matchmaking_round(ordered_list)
        matches_docid_list = MatchController.create_matches(matchmaking)
        r_docid = RoundController.create_round(matches_docid_list,
                                               current_round)
        return r_docid

    def create_round(matches_docid_list, current_round):
        round_name = Round.round_name(current_round)
        start_time = Round.time_round()
        round = Round(round_name, current_round,
                      matches_docid_list, start_time)
        r_docid = Round.create_round(round)
        return r_docid

    def get_last_round_docid(tournament_id):
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        r_docid_list = tournament['rounds_list']
        last_round_docid = r_docid_list[-1]
        return last_round_docid

    def update_rounds_list(tournament_id, r_docid):
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        rounds_list = tournament['rounds_list']
        rounds_list.append(r_docid)
        Tournament.update_rounds_list(None, rounds_list, tournament_id)

    def attribute_results(title, r_doc_id):
        menu = RoundMenu(app_title=title)
        Cli.clear_screen()
        Cli.cli_entry(title)
        print("Attribute results to Match")

        # Append Match in choices form
        round = Round.get_round_with_doc_id(r_doc_id)
        for match_doc_id in round['matches_list']:
            match = Match.get_matches_w_doc_id(match_doc_id)

            # Get Player with DOC ID
            player1 = match['p_one']
            player1_i = Player.get_player_w_docid(player1)
            player2 = match['p_two']
            player2_i = Player.get_player_w_docid(player2)

            menu.attribute_results_form[0]['choices'].append(
                {
                    'key': 'm',
                    'name': '{} {} ({}) vs {}  {} ({})'
                    .format(player1_i['name'],
                            player1_i['first_name'],
                            match['p_one_score'],
                            player2_i['name'],
                            player2_i['first_name'],
                            match['p_two_score']),
                    'value': match_doc_id
                }
            )

        answers = menu.attribute_results()
        match_results = answers['match_results']

        if answers['confirm']:
            MatchController.ask_winner(title, match_results)
            if answers['confirm']:
                Cli.cli_entry(title)
                RoundController.end_round_menu(title, r_doc_id)
                Cli.clear_screen()

    def end_round_menu(title, r_doc_id):
        menu = RoundMenu(app_title=title)
        answers = menu.end_round()

        if not answers['confirm']:
            RoundController.attribute_results(title, r_doc_id)

        elif answers['confirm']:
            end_time = Round.time_round()
            RoundController.update_end_time(r_doc_id, end_time)
            pass

    def update_end_time(r_doc_id, end_time):
        get_round = Round.get_round_with_doc_id(r_doc_id)
        round_object = Round.deserialize_round(get_round)
        round_object.update_end_round(end_time, r_doc_id)
