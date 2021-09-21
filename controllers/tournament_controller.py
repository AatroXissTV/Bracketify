# tournament_controller.py
# Created Sep 20, 2021 at 13:00 CEST
# Last updated Sep 21, 2021 at 10:16 CEST

# Standard imports

# Third-party imports

# Local imports
from controllers.round_controller import RoundController
from models.tournament_model import Tournament
from models.player_model import Player
from views.menu import Menu
from views.cli_view import Cli

# Other imports


class TournamentController():
    """Manage all tournaments related Models/views

    - Methods:
        create_tournament(self, title):
            This method is used to create tournament in 'tournaments' DB.
            Return DOC ID of tournament.

        launch_tournament(self, title):
            This method is used to launch a tournament created in
            'tournaments' DB.

        tournament(self, title, tournament_id):
            This method is used to iterate through rounds in tournament

        end_tournament(self, title):
            This method is used to end tournament.

        display_tournaments(self):
            This method is used to display list of tournaments to the user

                Calls:
                -> Tournament Modle -> load DB, deserialize

        display_players_in_t(self, title):
            This Method is used to display the list of the players
            in a tournaments
                Calls:
                -> Tournament model -> load DB, get tournament with name
                -> Player model -> Get player with doc ID
                -> launch_tournament_menu -> display form
    """

    def create_tournament(self, title):
        menu = Menu(app_title=title)
        print("Add a tournament in 'tournaments' DB.")

        # Append Choices in form with players list
        players_list = Player.load_players_db()
        for player in players_list:
            doc_id = Player.get_player_doc_id(player['name'])
            menu.tournament_form[7]['choices'].append(
                {
                    'key': 'd',
                    'name': '{} {} (rank {})'.format(player['first_name'],
                                                     player['name'],
                                                     player['rank']),
                    'value': doc_id,
                }
            )

        # Prompt form + Save in DB
        answers = menu.tournament_menu()
        if answers['confirm']:
            obj = Tournament.deserialize_tournament(answers)
            tournament_id = obj.create_tournament()
        return tournament_id

    def launch_tournament(self, title):
        menu = Menu(app_title=title)
        print("Launch a tournament")

        # Append choices in form with tournaments list
        tournaments_list = Tournament.load_tournaments_db()
        for t in tournaments_list:
            doc_id = Tournament.get_tournament_doc_id(t['name'])
            menu.launch_form[0]['choices'].append(
                {
                    'key': 't',
                    'name': "{} ({} rounds)".format(t['name'],
                                                    t['rounds_number']),
                    'value': doc_id
                }
            )

        # Prompt form
        answers = menu.launch_tournament_menu()
        tournament_id = answers['selected_t']

        if answers['confirm']:
            return tournament_id

    def first_round(self, title, tournament_id):
        menu = Menu(app_title=title)

        Cli.cli_entry(title)
        answers = menu.start_round()
        r_doc_id = RoundController.first_round(tournament_id)
        TournamentController.update_rounds_list(tournament_id, r_doc_id)
        Cli.cli_delay()

        if answers['confirm']:

            Cli.cli_entry(title)
            RoundController.attribute_results_round(title, r_doc_id)
            Cli.clear_screen()
        return r_doc_id

    def rounds(self, title, tournament_id, r_doc_id):
        menu = Menu(app_title=title)
        t = Tournament.get_tournament_with_doc_id(tournament_id)
        numb_of_rounds = t['rounds_number']

        for i in range(2, numb_of_rounds+1):
            print(i)
            Cli.cli_entry(title)
            answers = menu.start_round()
            if answers['confirm']:
                Cli.cli_entry(title)
                next_r_doc_id = RoundController.round(r_doc_id, i)
                print(next_r_doc_id)
                Cli.cli_delay()

            if answers['confirm']:
                Cli.cli_entry(title)
                RoundController.attribute_results_round(title, next_r_doc_id)
                Cli.cli_delay

    def end_tournament(self, title):
        menu = Menu(app_title=title)
        Cli.cli_entry(title)
        answers = menu.start_round()
        return answers

    def update_rounds_list(tournament_id, r_doc_id):
        Tournament.update_round_list(tournament_id, r_doc_id)

    def display_tournaments(self):
        print("List of tournaments")
        tournaments_list = Tournament.load_tournaments_db()
        for tournament in tournaments_list:
            obj = Tournament.deserialize_tournament(tournament)
            print(obj)

    def display_player_in_t(self, title):
        launch = Menu(app_title=title)
        print("Select a tournament")

        # Append choices with tournaments_list
        display_t = Tournament.load_tournaments_db()
        for tournament in display_t:
            launch.launch[0]['choices'].append(tournament['name'])

        answers = launch.launch_tournament_menu()

        if answers['confirm']:
            t = Tournament.get_tournament_w_name(answers['selected_t'])
            i = t['players_list']
            players_list = []
            for docid in i:
                test = Player.get_player_with_doc_id(docid)
                players_list.append(test)
            return players_list
