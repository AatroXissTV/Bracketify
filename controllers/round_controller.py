# round_controller.py
# Created Sep 13, 2021 at 15:00
# Last Updated Sep 15, 2021 at 15:11

# Standard imports

# Local imports
from views.cli_view import Cli
from models.rounds_model import Round
from views.menu import Menu
from models.tournament_model import Tournament
from models.player_model import Player
from models.match_model import Match

# Other imports


class RoundController():

    def get_players_round(tournaments_list):
        print("Matchmaking for the first round of the tournament")
        t = Tournament.get_tournament_w_name(tournaments_list)
        players_docid = t['players_list']
        players_list = []
        for docid in players_docid:
            player = Player.get_player_with_doc_id(docid)
            players_list.append(player)
        order_players_rank = Player.get_players_ordered_by_rank(players_list)
        return order_players_rank

    def middle_index_players_list(players_in_round):
        length = len(players_in_round)
        middle_index = length//2
        return middle_index

    def split_first_half_p(players_in_round, middle_index):
        first_half = players_in_round[:middle_index]
        return first_half

    def split_second_half_p(players_in_round, middle_index):
        second_half = players_in_round[middle_index:]
        return second_half

    def mm_first_round(middle_index, first_half, second_half):

        print("Generating Matches for the first round")
        matches_list = []

        for i in range(middle_index):
            match = Match(first_half[i]['first_name'],
                          second_half[i]['first_name'])
            print(match)
            serialize_match = match.serialize_match()
            matches_list.append(serialize_match)
        return matches_list

    def ask_winner(title, matches_list, middle_index):
        print("Enter the winner of the round")
        matches_tuple = []
        for i in range(middle_index):
            Cli.cli_entry(title)
            match = Match(matches_list[i]['p_one'],
                          matches_list[i]['p_two'],
                          matches_list[i]['p_one_score'],
                          matches_list[i]['p_two_score'])
            print(match)
            menu = Menu(app_title=title)
            ask_winner_menu = menu.ask_winner()

            if (ask_winner_menu == "0"):
                match.match_results("0")
                print(match)

            elif (ask_winner_menu == "1"):
                match.match_results("1")
                print(match)

            elif (ask_winner_menu == "2"):
                match.match_results("2")
                print(match)

            tuple = match.create_match_tuple()
            matches_tuple.append(tuple)
        return matches_tuple

    def end_first_round(start_time, matches_results):
        end_time = Round.end_round()
        round = Round("Round", 1, matches_results, start_time, end_time)
        serialized_round = round.serialize_round()
        return serialized_round
