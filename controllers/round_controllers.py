# controllers/round_controllers.py
# created 24/09/2021 @ 11:12 CEST
# last updated 28/09/2021 @ 13:16 CEST

""" controllers/round_controller.py

To do:
    * Add tasks
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "1.0.1"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports
from time import sleep

# third-party imports

# local imports
from models.player_models import Player
from models.tournament_models import Tournament
from models.round_models import Round
from models.match_models import Match
from views.cli_views import Cli
from views.tournament_views import TournamentMenu
from views.round_views import RoundMenu
from controllers.match_controllers import MatchController

# other


class RoundController():
    """this class represents the round controller of Bracketify
    Summary of methods and quick explanation:

    - Methods :
        go_next_round(tournament_id, rounds_number, len_rounds_list):
            used to go to next round if its the first round launch first_round
            else launch round.

        attribute_results(tournament_id, title, r_docid):
            used to know to which player the user wants to attribute scores.

        end_round_menu(tournament_id, title, r_docid):
            used to know if the user wants to end the round

        first_round(tournament_id, current_round):
            used to manage the pairing & creation of first round

        round(tournament_id, current_round, last_round_docid):
            used to manage the pairing & creation of rounds.

        create_round(matches_docid_list, current_round):
            create round in 'rounds' DB.

        update_end_time(r_docid, end_time):
            used to update end_time of a round.

        update_rounds_list(tournament_id, r_docid):
            used to update rounds_list in tournament.
    """

    def go_next_round(tournament_id, current_round, len_rounds_list, title):
        round_type = Round.determine_round_type(len_rounds_list)
        if (round_type == "first_round"):
            r_docid = RoundController.first_round(tournament_id, current_round)
            RoundController.update_rounds_list(tournament_id, r_docid)
            RoundController.attribute_results(tournament_id, title, r_docid)
            return r_docid
        else:
            last_r_docid = RoundController.get_last_round_docid(tournament_id)
            r_docid = RoundController.round(tournament_id, current_round,
                                            last_r_docid)
            RoundController.update_rounds_list(tournament_id, r_docid)
            RoundController.attribute_results(tournament_id, title, r_docid)
            return r_docid

    # ATTRIBUTE RESULTS

    def attribute_results(tournament_id, title, r_docid):
        menu = RoundMenu(app_title=title)
        Cli.cli_entry(title)
        print("Attribute results to Match")

        # Append Match in choices form
        round = Round.get_round_with_doc_id(r_docid)
        for match_docid in round['matches_list']:
            match = Match.get_matches_w_doc_id(match_docid)

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
                    'value': match_docid
                }
            )

        answers = menu.attribute_results()

        if answers['confirm']:
            MatchController.ask_winner(title, answers['match_results'])
            end_r_answer = RoundController.end_round_menu(tournament_id,
                                                          title,
                                                          r_docid)
            round = Round.get_round_with_doc_id(r_docid)
            if end_r_answer['confirm']:
                for match_docid in round['matches_list']:
                    get_match = Match.get_matches_w_doc_id(match_docid)
                    if get_match['p_one_score'] is None:
                        print("\n!!! Please assign scores to all matches !!!")
                        sleep(5)
                        RoundController.attribute_results(tournament_id, title,
                                                          r_docid)
                    else:
                        MatchController.calculate_points(match_docid)
                pass
            else:
                pass
        else:
            pass

    def end_round_menu(tournament_id, title, r_doc_id):
        menu = RoundMenu(app_title=title)
        answers = menu.end_round()

        if not answers['confirm']:
            RoundController.attribute_results(tournament_id, title, r_doc_id)

        elif answers['confirm']:
            end_time = Round.time_round()
            RoundController.update_end_time(r_doc_id, end_time)
            pass

        return answers

    # ROUNDS

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
        matchmaking = MatchController.matchmaking_round(ordered_list,
                                                        tournament_id)
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

    def update_end_time(r_docid, end_time):
        get_round = Round.get_round_with_doc_id(r_docid)
        round_object = Round.deserialize_round(get_round)
        round_object.update_end_round(end_time, r_docid)

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

    # DISPLAY

    def display_r_in_t(title):
        Cli.cli_entry(title)
        tournament_menu = TournamentMenu(app_title=title)
        print("Select a tournament\n")

        # Append choices with tournaments list
        tournament_docid_list = Tournament.load_tournament_docid_db()

        for t_docid in tournament_docid_list:
            tournament = Tournament.get_tournament_w_docid(t_docid)
            tournament_menu.select_tournament_form[0]['choices'].append(
                {
                    'key': 't',
                    'name': 'Name: {} - Location: {} - Dates: {} - {}'
                    .format(tournament['name'],
                            tournament['location'],
                            tournament['start_date'],
                            tournament['end_date']),
                    'value': t_docid
                }
            )

        answers = tournament_menu.select_tournament()
        if answers['confirm']:

            t = Tournament.get_tournament_w_docid(answers['selected_t'])
            r_docid_list = t['rounds_list']
            for r_docid in r_docid_list:
                round = Round.get_round_with_doc_id(r_docid)
                round_object = Round.deserialize_round(round)
                print(round_object)
