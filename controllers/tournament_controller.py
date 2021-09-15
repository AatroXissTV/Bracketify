# tournament_controller.py
# Created Sep 10, 2021 at 11:10
# Last Updated Sep 15, 2021 at 15:11

# Standrad imports

# local imports
from views.cli_view import Cli
from models.rounds_model import Round
from models.player_model import Player
from models.tournament_model import Tournament
from views.menu import Menu
from controllers.round_controller import RoundController

# Other imports


class TournamentController():

    """ Summary of Methods used in Tournament Controller

    - Methods :
        create_tournament(self, title)
            This method is used to manage creation of tournaments.
            Display menu, manage answers &
            save the tournaments in 'tournaments' DB.
    """

    def create_tournament(self, title):
        tournament_menu = Menu(app_title=title)
        print("Add a tournament to the 'tournaments' DB.")

        # Append choices with players list
        display_p = Player.load_players_db()

        for player in display_p:

            # Value is DOC ID of a player
            doc_id = Player.get_player_doc_id(player['name'])

            tournament_menu.tournament_form[7]['choices'].append(
                {
                    'key': 'd',
                    'name': '{} {} (rank {})'.format(player['first_name'],
                                                     player['name'],
                                                     player['rank']),
                    'value': doc_id,
                },
            )

        # prompt form + saves it in DB
        answers = tournament_menu.tournament_menu()
        if answers['confirm']:
            obj = Tournament.deserialize_tournament(answers)
            obj.create_tournament()

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

    def launch_tournament(self, title):
        launch = Menu(app_title=(title))
        print("Launch a tournament.")

        # Append Choices with tournaments list
        display_t = Tournament.load_tournaments_db()
        for tournament in display_t:
            launch.launch[0]['choices'].append(tournament['name'])

        answers = launch.launch_tournament_menu()

        if answers['confirm']:
            Cli.cli_entry(title)
            p_sorted = RoundController.get_players_round(answers['selected_t'])
            middle_index = RoundController.middle_index_players_list(p_sorted)
            first_half = RoundController.split_first_half_p(p_sorted,
                                                            middle_index)
            second_half = RoundController.split_second_half_p(p_sorted,
                                                              middle_index)
            mm_round = RoundController.mm_first_round(middle_index,
                                                      first_half,
                                                      second_half)
            Cli.cli_delay()

            Cli.cli_entry(title)
            start_time = Round.start_round()
            match_tuple = RoundController.ask_winner(title,
                                                     mm_round,
                                                     middle_index)
            Cli.cli_delay()
            Cli.cli_entry(title)
            end = RoundController.end_first_round(start_time, match_tuple)
            print(end)
