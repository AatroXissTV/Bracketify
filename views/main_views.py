# views/main_views.py
# created 22/09/2021 @ 22:24 CEST
# last updated 22/09/2021 @ 22:24 CEST

# must be at the beginning of the file
from __future__ import print_function, unicode_literals

""" views/main_views.py

To do:
    * Update Requirements with PyInquirer.
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
from PyInquirer import style_from_dict, Token, prompt

# local imports
from views.cli_views import Cli

# other


class MainMenu(Cli):
    """This class represents the main menu of bracketify

    - Herit from Cli (cli_views.py)
    """

    def __init__(self, app_title):
        super().__init__(app_title)
        """Constructor

        app_title -> str
        """

        self.style = style_from_dict({
            Token.Answer: '#568259',
            Token.Question: '',  # Default
            Token.Instruction: '#E63946',
            Token.Pointer: '#F1FAEE'
        })

        self.main_menu_form = [
            {
                'type': 'list',
                'name': 'main_menu',
                'message': "Select: ",
                'choices': ["Add a new player",
                            "Changes a player's rank",
                            "Add a new tournament",
                            "Launch a tournament",
                            "View reports",
                            "Quit"]
            }
        ]

        self.reports_submenu_form = [
            {
                'type': 'list',
                'name': 'reports_submenu',
                'message': "Select the type of reports you want to display",
                'choices': ["players",
                            "tournaments",
                            "players in a tournament",
                            "all rounds in a tournament",
                            "all the matches of a tournament",
                            "return to main menu"]
            }
        ]

        self.order_submenu_form = [
            {
                'type': 'list',
                'name': 'ordered_submenu',
                'message': 'Select how you want to display the data',
                'choices': ["by alphabetical order (a -> z)",
                            "by alphabetical order (z -> a)",
                            "by rank order (1 -> x)",
                            "by rank order (x -> 1)",
                            "return to reports menu"]
            }
        ]

        self.return_to_main_form = [
            {
                'type': 'confirm',
                'name': 'return_to_main',
                'message': 'Do you want to return to main menu ?',
                'default': True
            }
        ]

    """Summary of methods and quick explanation

    - Methods:
        main_menu(self):
            used to prompt main_menu_form
            Return a dict() of the answer

        reports_submenu(self)
            used to prompt reports form
            return a dict() of the answer

        order_subement(self):
            used to prompt order form
            return a dict() of the answer

        return_to_main_menu(self):
            used to return to main menu after displaying reports
    """

    def main_menu(self):
        main_menu = self.main_menu_form
        answers = prompt(main_menu, style=self.style)
        return answers['main_menu']

    def reports_submenu(self):
        reports_submenu = self.reports_submenu_form
        answers = prompt(reports_submenu, style=self.style)
        return answers['reports_submenu']

    def order_submenu(self):
        order_submenu = self.order_submenu_form
        answers = prompt(order_submenu, style=self.style)
        return answers['ordered_submenu']

    def return_to_main(self):
        return_to_main_form = self.return_to_main_form
        answers = prompt(return_to_main_form, style=self.style)
        return answers['return_to_main']
