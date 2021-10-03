# controllers/tournament_controllers.py
# created 23/09/2021 @ 10:33 CEST
# last updated 28/09/2021 @ 10:10 CEST

""" controllers/tournament_controller.py

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
from controllers.player_controllers import PlayerController
from controllers.match_controllers import MatchController
from controllers.round_controllers import RoundController

# other


class TournamentController():
    """this class represents the
       tournament controller of Bracketify

    Manages menus that are tournament related
    """

    def add_a_new_tournament_menu(title):
        Cli.cli_entry(title)
        tournament_menus = TournamentMenu(app_title=title)
        print("You can now add a new tournament in the 'tournament' DB.")
        print("Please enter the requested information\n")

        # load player in choices.
        players_docid_list = Player.load_players_docid_db()
        players_list = []
        for player_docid in players_docid_list:
            player = Player.get_player_w_docid(player_docid)
            players_list.append(player)
            tournament_menus.add_a_tournament_form[7]['choices'].append(
                {
                    'key': 'p',
                    'name': '{} {} ({})'
                    .format(player['name'],
                            player['first_name'],
                            player['rank']),
                    'value': player_docid
                }
            )

        answers = tournament_menus.add_a_new_tournament()
        if answers['confirm']:
            obj = Tournament.deserialize_tournament(answers)
            obj.create_tournament()
            Cli.cli_delay()
        else:
            print("\nThe tournament has not been added to the database\n")
            Cli.cli_delay_no_interaction()
            pass

    def launch_a_tournament(title):
        Cli.cli_entry(title)
        tournament_menu = TournamentMenu(app_title=title)
        print("You can now launch a tournament")
        print("Please select first a tournament\n")

        # Append choices with tournaments list
        tournament_docid_list = Tournament.load_tournament_docid_db()
        for t_docid in tournament_docid_list:
            tournament = Tournament.get_tournament_w_docid(t_docid)
            actual_round = len(tournament['rounds_list'])
            round_number = tournament['rounds_number']
            tournament_menu.select_tournament_form[0]['choices'].append(
                {
                    'key': 't',
                    'name': '{} | {} - {} | Start -> Round {} | Round Numb {}'
                    .format(tournament['name'],
                            tournament['start_date'],
                            tournament['end_date'],
                            actual_round,
                            round_number),
                    'value': t_docid
                }
            )

        answers = tournament_menu.select_tournament()
        if answers['confirm']:
            TournamentController.t_rounds_management(answers['selected_t'],
                                                     title)
            Cli.cli_delay()
        else:
            print("\n You have chosen not to launch a tournament.")
            print("back to the main menu")
            Cli.cli_delay_no_interaction()
            pass

    def t_rounds_management(tournament_id, title):
        round_menu = RoundMenu(app_title=title)
        tournament = Tournament.get_tournament_w_docid(tournament_id)
        rounds_number = tournament['rounds_number']
        len_rounds_list = Tournament.get_len_rounds_list(tournament_id)

        while (len_rounds_list < (rounds_number)):
            Cli.cli_entry(title)
            answers = round_menu.start_round()

            if answers['confirm']:
                current_round = len_rounds_list+1
                RoundController.go_next_round(tournament_id,
                                              current_round,
                                              len_rounds_list, title)
                len_rounds_list = Tournament.get_len_rounds_list(tournament_id)
            else:
                print("The round has not started.")
                print("We redirect you to the main menu")
                Cli.cli_delay_no_interaction()

        else:
            Cli.cli_entry(title)
            menu = RoundMenu(app_title=title)
            print("The tournament is finished.")
            print("Players list by total points\n")
            r_docid = RoundController.get_last_round_docid(tournament_id)
            matches_tuples = MatchController.get_match_tuples(r_docid)
            ordered_list = MatchController.sort_players_round(matches_tuples)
            for player in ordered_list:
                get_player = Player.get_player_w_docid(player[0])
                print("{} {} ({}) - Total {}".format(get_player['first_name'],
                                                     get_player['name'],
                                                     get_player['rank'],
                                                     player[1]))
            answers = menu.results()
            if answers['confirm']:
                PlayerController.modify_player_in_t_rank(title, ordered_list)
            else:
                print("Back to main menu")
                sleep(3)
                pass

    # DISPLAY

    def display_tournaments(title):
        Cli.cli_entry(title)
        print("List of tournaments\n")
        tournament_docid_list = Tournament.load_tournament_docid_db()
        tournament_list = []
        for tournament_id in tournament_docid_list:
            tournament_str = Tournament.get_tournament_w_docid(tournament_id)
            tournament_list.append(tournament_str)
        for tournament in tournament_list:
            tournament = Tournament.deserialize_tournament(tournament)
            print(tournament)

    def display_p_in_t(title):
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
            p_docid_list = t['players_list']
            players_list = []
            for p_docid in p_docid_list:
                player = Player.get_player_w_docid(p_docid)
                players_list.append(player)
            return players_list
        else:
            print("You have not selected a tournament")
            print("You will be redirected to main menu")
            Cli.cli_delay_no_interaction()
            pass

    def display_m_in_t(title):
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
                print("\n")
                print(round_object)
                for m_docid in round['matches_list']:
                    match = Match.get_matches_w_doc_id(m_docid)
                    player1 = Player.get_player_w_docid(match['p_one'])
                    player2 = Player.get_player_w_docid(match['p_two'])
                    print("P1: {} {} ({}) vs P2: {} {} ({})"
                          .format(player1['name'], player1['first_name'],
                                  match['p_one_score'],
                                  player2['name'], player2['first_name'],
                                  match['p_two_score']))
        else:
            print("You have not selected a tournament")
            print("You will be redirected to main menu")
            Cli.cli_delay_no_interaction()
