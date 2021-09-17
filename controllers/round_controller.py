# round_controller.py
# Created Sep 13, 2021 at 15:00
# Last Updated Sep 17, 2021 at 14:30

# Standard imports

# Local imports
from views.cli_view import Cli
from controllers.match_controller import MatchContoller
from models.match_model import Match
from models.rounds_model import Round
from models.tournament_model import Tournament
from models.player_model import Player
from views.menu import Menu

# Other imports


class RoundController():

    def get_players(tournaments_list):
        print("Matchmaking for the first round of the tournament")
        t = Tournament.get_tournament_w_name(tournaments_list)
        players_docid = t['players_list']
        players_list = []
        for docid in players_docid:
            player = Player.get_player_with_doc_id(docid)
            players_list.append(player)
        order_players_rank = Player.get_players_ordered_by_rank(players_list)
        return order_players_rank

    def get_numb_rounds(tournaments_list):
        t = Tournament.get_tournament_w_name(tournaments_list)
        numb_of_rounds = t['rounds_number']
        return numb_of_rounds

    def get_middle_index(players_in_round):
        middle_index = Round.middle_index_players_list(players_in_round)
        return middle_index

    def mm_first_round(players_in_round, middle_index):
        first_half = Round.split_first_half(players_in_round, middle_index)
        second_half = Round.split_second_half(players_in_round, middle_index)

        matches_list = Round.mm_first_round(middle_index,
                                            first_half,
                                            second_half)
        return matches_list

    def create_round(matches_list, round_number):
        round_name = Round.round_name(round_number)
        start_time = Round.start_round()
        round = Round(round_name, 1, matches_list, start_time)
        round_doc_id = Round.create_round(round)
        return round_doc_id

    def get_round_with_doc_id(round_doc_id):
        round = Round.get_round_with_doc_id(round_doc_id)
        return round

    def c_first_round(title, selected_t):
        p_sorted = RoundController.get_players(selected_t)
        middle_index = RoundController.get_middle_index(p_sorted)
        matchmaking = RoundController.mm_first_round(p_sorted,
                                                     middle_index)

        matches_list = []
        for matches in matchmaking:
            deserialized = Match.deserialize_matches(matches)
            match_doc_id = Match.create_match(deserialized)
            matches_list.append(match_doc_id)

        first_r_doc_id = RoundController.create_round(matches_list, 1)
        return first_r_doc_id

    def attribute_results(sef, title, r_doc_id):
        menu = Menu(app_title=title)
        print("Attribute results to match")

        round = RoundController.get_round_with_doc_id(r_doc_id)

        for match_doc_id in round['matches_list']:
            match = Match.get_matches_w_doc_id(match_doc_id)

            menu.attribute_results_form[0]['choices'].append(
                {
                    'key': 'm',
                    'name': '{} ({}) vs {} ({})'
                    .format(match['p_one'],
                            match['p_one_score'],
                            match['p_two'],
                            match['p_two_score']),
                    'value': match_doc_id
                }
            )

        answers = menu.attribute_results()
        match_selected = answers['match_results']

        if answers['confirm']:
            MatchContoller.ask_winner(title, match_selected)

            if answers['confirm']:
                Cli.cli_entry(title)
                RoundController.end_round_menu(None, title, r_doc_id)
                Cli.clear_screen()

    def end_round_menu(self, title, r_doc_id):
        menu = Menu(app_title=title)
        answers = menu.end_round()

        if not answers['confirm']:
            RoundController.attribute_results(None, title, r_doc_id)

        elif answers['confirm']:
            pass

    def end_first_round(start_time, matches_results):
        end_time = Round.end_round()
        round = Round("Round", 1, matches_results, start_time, end_time)
        serialized_round = round.serialize_round()
        return serialized_round
