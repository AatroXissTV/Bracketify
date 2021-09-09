# main_menu.py
# Created Sep 03, 2021 at 14:42
# Last updated Sep 08, 2021 at 16:07

# Standard imports

# Third-party imports
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt

# Local imports
from views.cli_view import Cli

# Other imports


class MainMenu(Cli):
    """Represents the menu of Bracketify.

    - Heritage :
        MainMenu class herits from Cli.
    """
    def __init__(self, app_title):
        super().__init__(app_title)

        # Style of the Menu
        self.style = style_from_dict({
            Token.Answer: '#26FFDF',
            Token.Question: '',  # Default
            Token.Instruction: '#F26A1B',
            Token.Pointer: '#08A696 bold',
        })

        # Main Menu
        self.main_menu_form = [
            {
                'type': 'list',
                'name': 'main_menu',
                'message': 'Whalecome to Bracketify',
                'choices': ['Add a player',
                            'Modify a player rank',
                            'Add a tournament',
                            'Launch a tournament',
                            'Display Infos',
                            'Quit']
            },
        ]

        # Modify Rank Form
        self.modify_rank_form = [
            {
                'type': 'list',
                'name': 'name',
                'message': 'Select the player to edit.',
                'choices': [],
            },
            {
                'type': 'input',
                'name': 'new_rank',
                'message': 'Enter the new rank.',
                'filter': lambda val: int(val) if int(val) > 0 else None
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False,
            }
        ]

        # Tournament From
        self.tournament_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': "Tournament's name : ",
            },
            {
                'type': 'input',
                'name': 'location',
                'message': 'location',
            },
            {
                'type': 'input',
                'name': 'start_date',
                'message': "Start Date",
            },
            {
                'type': 'input',
                'name': 'end_date',
                'message': "End Date",
            },
            {
                'type': 'input',
                'name': 'description',
                'message': 'Comments',

            },
            {
                'type': 'list',
                'name': 'rules',
                'message': 'Select the tournaments rules',
                'choices': ["Bullet", "Blitz", "Rapid"],
            },
            {
                'type': 'input',
                'name': 'rounds_number',
                'message': 'Numb of rounds > 0 or set to 4',
                'default': '4',
                'filter': lambda val: int(val) if int(val) > 0 else None,
            },
            {
                'type': 'checkbox',
                'message': 'Select players participating',
                'name': 'players_list',
                'choices': [],
                'validate': lambda choices: 'Select 8 players min'
                if len(choices['players_list']) < 8 else True,
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False,
            }
        ]

    """Methods used MainMenu class

    - Method :
    """

    def main_menu(self):
        main_menu = self.main_menu_form
        answers = prompt(main_menu, style=self.style)
        return answers['main_menu']

    def player_menu(self):
        player_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': "last name: ",
            },
            {
                'type': 'input',
                'name': 'first_name',
                'message': "first name: ",
            },
            {
                'type': 'input',
                'name': 'birth_date',
                'message': "birth date: ",
            },
            {
                'type': 'list',
                'name': 'gender',
                'message': 'gender: ',
                'choices': ['Male', 'Female', 'Other'],
            },
            {
                'type': 'input',
                'name': 'rank',
                'message': 'rank',
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False
            },
        ]
        answers = prompt(player_form, style=self.style)
        return answers

    def modify_rank_menu(self):
        modify_rank_form = self.modify_rank_form
        answers = prompt(modify_rank_form, style=self.style)
        return answers

    def tournament_menu(self):
        tournament_form = self.tournament_form
        answers = prompt(tournament_form, style=self.style)
        return answers

    def launch_tournament_menu(self):
        launch_form = [
            {
                'type': 'list',
                'name': 'tournaments_list',
                'message': "Select the tournament to launch",
                'choices': [],
            }
        ]
        answers = prompt(launch_form, style=self.style)
        return answers

    def display_infos_menu(self):
        display_infos_form = [
            {
                'type': 'list',
                'name': 'display_infos',
                'message': 'Select your option to display',
                'choices': ["All players",
                            "All tournaments",
                            "All players of a tournament",
                            "All rounds of a tournament",
                            "All matches of a tournament",
                            "Return to main menu", ]
            }
        ]
        answers = prompt(display_infos_form, style=self.style)
        return answers

    def quit_menu(self):
        exit()