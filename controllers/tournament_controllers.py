# controllers/tournament_controllers.py
# created 23/09/2021 @ 10:33 CEST
# last updated 23/09/2021 @ 10:33 CEST

""" controllers/tournament_controller.py

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
from controllers.round_controllers import RoundController
from models.player_models import Player
from models.tournament_models import Tournament
from views.cli_views import Cli
from views.tournament_views import TournamentMenu

# other


class TournamentController():
    """this class represents the
       tournament controller of Bracketify

    Manages menus that are tournament related
    """

    def add_a_new_tournament_menu(title):
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
            Cli.cli_delay

        else:
            print("\nThe player has not been added to the database\n")
            Cli.cli_delay_no_interaction()
            pass

    def launch_a_tournament(title):
        tournament_menu = TournamentMenu(app_title=title)
        print("You can now launch a tournament")
        print("Please select first a tournament\n")

        # Append choices with tournaments list
        tournament_docid_list = Tournament.load_tournament_docid_db()

        for t_docid in tournament_docid_list:
            tournament = Tournament.get_tournament_w_docid(t_docid)
            actual_round = len(tournament['rounds_list'])
            tournament_menu.select_tournament_form[0]['choices'].append(
                {
                    'key': 't',
                    'name': '{} | Dates: {} - {} | Start from round {}'
                    .format(tournament['name'],
                            tournament['start_date'],
                            tournament['end_date'],
                            actual_round),
                    'value': t_docid
                }
            )

        answers = tournament_menu.select_tournament()
        if answers['confirm']:
            RoundController.rounds_management(answers['selected_t'], title)
            Cli.cli_delay()
        else:
            pass

    def display_tournaments(self):
        print("List of tournaments\n")
        tournament_docid_list = Tournament.load_tournament_docid_db()
        tournament_list = []
        for tournament_id in tournament_docid_list:
            tournament_str = Tournament.get_tournament_w_docid(tournament_id)
            tournament_list.append(tournament_str)
        for tournament in tournament_list:
            tournament = Tournament.deserialize_tournament(tournament)
            print(tournament)

    def display_p_in_t(self, title):
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
