# round_controller.py
# Created Sep 13, 2021 at 15:00
# Last Updated Sep 16, 2021 at 10:29

# Standard imports

# Local imports
from models.rounds_model import Round
from models.tournament_model import Tournament
from models.player_model import Player

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

    def end_first_round(start_time, matches_results):
        end_time = Round.end_round()
        round = Round("Round", 1, matches_results, start_time, end_time)
        serialized_round = round.serialize_round()
        return serialized_round
