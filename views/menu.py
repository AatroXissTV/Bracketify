# menu.py
# Created Sep 03, 2021 at 14:42
# Last updated Sep 13, 2021 at 09:24

# Standard imports

# Third-party imports
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt

# Local imports
from views.cli_view import Cli

# Other imports


class Menu(Cli):
    """Represents the menus of Bracketify.

    - Heritage :
        Menu class herits from Cli.
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

        # MAIN MENU
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

        # DISPLAY SUBMENU
        self.display_menus = [
            {
                'type': 'list',
                'name': 'display_menus',
                'message': "Here you can check all datas.",
                'choices': ['Players', 'Tournaments',
                            'Return']
            },
        ]

        # ORDER SUBMENU
        self.sorted_menus_items = [
            {
                'type': 'list',
                'name': 'sorted_items',
                'message': "How do you want to display data? ",
                'choices': ['By alphabetical order (a -> z)',
                            'By rank order (1 -> x)',
                            'Return']
            },
        ]

        # RETURN MENU
        self.return_to_main_form = [
            {
                'type': 'confirm',
                'name': 'return_to_main',
                'message': 'Do you want to return to main menu ?',
                'default': True
            }
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

        # Player Form
        self.player_form = [
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

        # Launch form
        self.launch = [
            {
                'type': 'list',
                'name': 'selected_t',
                'message': 'Select the tournament.',
                'choices': [],
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False,
            }
        ]

        # Who won form
        self.ask_winner_form = [
            {
                'type': 'list',
                'name': 'ask_winner',
                'message': "Select Winner (tie = 0, P1 = 1, P2 = 2)",
                'choices': ['0', '1', '2']
            },
            {
                'type': 'confirm',
                'name': 'confirm',
                'message': 'Are you sure to validate these fields ?',
                'default': False,
            }
        ]

    """Methods used Menu class

    - Methods :
        main_menu(self):
            This method is used to prompt main menu form to the user.
            Return a dict() with the result.
            This dict is then used by the controller to know where the user
            wants to navigate.

        player_menu(self):
            This method is used to prompt the player menu form to the user.

        modify_rank_menu(self):
            This method is used to prompt the modify rank form to the user.

        tournament_menu(self):
            This method is used to prompt the tournament form to the user

        launch_tournament_menu(self):
            This method is used to prompt the tournament form to the user

        display_menus_item(self):
            This method is used to prompt display menu to the user
            Return a dict() with the results
            This dict is then used by the controller to know what the user
            wants to do.

        sort_menus_item(self):
            This method is used to prompt sort menu to the user
            Return a dict() with the results
            This dict is then used by the controller to know how the user
            wants to order the datas.

        quit_menu(self):
            This method is used to close the app.
    """

    def main_menu(self):
        main_menu = self.main_menu_form
        answers = prompt(main_menu, style=self.style)
        return answers['main_menu']

    def player_menu(self):
        player_form = self.player_form
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
        launch_form = self.launch
        answers = prompt(launch_form, style=self.style)
        return answers

    def ask_winner(self):
        ask_winner = self.ask_winner_form
        answers = prompt(ask_winner, style=self.style)
        return answers['ask_winner']

    def display_menus_item(self):
        display_menus = self.display_menus
        answers = prompt(display_menus, style=self.style)
        return answers['display_menus']

    def sort_menus_items(self):
        sorted_menus = self.sorted_menus_items
        answers = prompt(sorted_menus, style=self.style)
        return answers['sorted_items']

    def return_to_main(self):
        return_to_main_form = self.return_to_main_form
        answers = prompt(return_to_main_form, style=self.style)
        return answers['return_to_main']

    def quit_menu(self):
        exit()
