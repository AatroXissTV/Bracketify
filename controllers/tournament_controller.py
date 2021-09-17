# tournament_controller.py
# Created Sep 10, 2021 at 11:10
# Last Updated Sep 17, 2021 at 10:20

# Standrad imports

# Third-party imports

# local imports
from models.match_model import Match
from controllers.round_controller import RoundController
from models.player_model import Player
from models.tournament_model import Tournament
from views.menu import Menu
from views.cli_view import Cli

# Other imports


class TournamentController():

    """ Summary of Methods used in Tournament Controller

    - Methods :
        create_tournament(self, title)
            This method is used to manage creation of tournaments.
            Display menu, manage answers &
            save the tournaments in 'tournaments' DB.

                Calls:
                It calls other methods in models & views
                -> Player model -> Load DB, Get player doc_id
                -> Tournament model -> deserialize, create tournament
                -> tournament menu (viewds) -> display form

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


        launc_tournament(self, title):
            This method is used to manage launch a tournament menus.
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

    # LAUNCH TOURNAMENT

    def launch_tournament(self, title):
        menu = Menu(app_title=title)
        print("Launching a tournament")

        # Append Choices with tournaments_list
        display_t = Tournament.load_tournaments_db()
        for tournament in display_t:
            menu.launch_form[0]['choices'].append(tournament['name'])

        answers = menu.launch_tournament_menu()
        selected_t = answers['selected_t']

        if answers['confirm']:
            Cli.cli_entry(title)
            answers = menu.start_round()

            # Matchmaking
            p_sorted = RoundController.get_players_round(selected_t)
            middle_index = RoundController.get_middle_index(p_sorted)
            matchmaking = RoundController.mm_first_round(p_sorted,
                                                         middle_index)

            matches_list = []
            for matches in matchmaking:
                deserialized = Match.deserialize_matches(matches)
                match_doc_id = Match.create_match(deserialized)
                matches_list.append(match_doc_id)

            # Create Round
            first_r_doc_id = RoundController.create_round(matches_list, 1)
            print(first_r_doc_id)

            if answers['confirm']:
                Cli.cli_entry(title)

                # Append Choices with Matches in round
                round = RoundController.get_round_with_doc_id(first_r_doc_id)

                for match_doc_id in round['matches_list']:
                    match_info = Match.get_matches_w_doc_id(match_doc_id)

                    menu.attribute_results_form[0]['choices'].append(
                        {
                            'key': 'm',
                            'name': '{} ({}) vs {} ({})'
                            .format(match_info['p_one'],
                                    match_info['p_one_score'],
                                    match_info['p_two'],
                                    match_info['p_two_score']),
                            'value': match_doc_id
                        }
                    )

                answers = menu.attribute_results()

                if answers['confirm']:
                    Cli.cli_entry(title)
                    match_selected = answers['match_results']
                    ask_winner_menu = menu.ask_winner()

                    if (ask_winner_menu == "0"):
                        serialize = Match.get_matches_w_doc_id(match_selected)
                        match = Match.deserialize_matches(serialize)
                        match.match_results("0")
                        serialized = match.serialize_match()
                        match.update_scores(serialized['p_one_score'],
                                            serialized['p_two_score'],
                                            match_selected)
                        print(match)

                    elif (ask_winner_menu == "1"):
                        serialize = Match.get_matches_w_doc_id(match_selected)
                        match = Match.deserialize_matches(serialize)
                        match.match_results("1")
                        serialized = match.serialize_match()
                        match.update_scores(serialized['p_one_score'],
                                            serialized['p_two_score'],
                                            match_selected)
                        print(match)

                    elif (ask_winner_menu == "2"):
                        serialize = Match.get_matches_w_doc_id(match_selected)
                        match = Match.deserialize_matches(serialize)
                        match.match_results("2")
                        serialized = match.serialize_match()
                        match.update_scores(serialized['p_one_score'],
                                            serialized['p_two_score'],
                                            match_selected)
                        print(match)

                    if answers['confirm']:
                        Cli.cli_entry(title)

                elif answers:
                    Cli.cli_entry(title)
                    answers = menu.end_round()
                    if answers['confirm']:
                        pass
