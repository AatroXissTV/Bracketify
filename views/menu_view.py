# menu_view.py
# Created Aug 31, 2021 at 15:37 CEST
# Last updated 31, 2021 at 15:37 CEST

# Standard imports

# Third-party imports

# Local imports

# Other imports

game_menu = [
    "Ajouter un tournoi",
    "Ajouter un joueur",
    "Modifier le classement d'un joueur",
    "Lancer un tournoi",
    "Afficher",
    "Quitter"
]


class Menu:
    def display_title(self):
        print("______                    _   _  __       ")  # noqa: W605
        print("| ___ \                  | | (_)/ _|      ")  # noqa: W605
        print("| |_/ /_ __ __ _  ___ ___| |_ _| |_ _   _ ")  # noqa: W605
        print("| ___ \ '__/ _` |/ __/ _ \ __| |  _| | | |")  # noqa: W605
        print("| |_/ / | | (_| | (_|  __/ |_| | | | |_| |")  # noqa: W605
        print("\____/|_|  \__,_|\___\___|\__|_|_|  \__, |")  # noqa: W605
        print("                                     __/ |")  # noqa: W605
        print("                                    |___/ ")  # noqa: W605

    def display_menu(self):
        choice = ""
        while True:
            try:
                print("[1] Ajouter un tournoi",
                      "[2] Ajouter un joueur",
                      "[3] Modifier le classement d'un joueur",
                      "[4] Lancer un tournoi",
                      "[5] Afficher",
                      "[6] Quitter",
                      "Votre choix : ",
                      sep='\n', end="")
                choice = int(input())
                if choice not in range(1, 7, 1):
                    print("Vous ne pouvez pas faire ça.\n")
                    continue
                else:
                    break
            except ValueError:
                print("Entrez un chiffre (1 - 7)")
                continue
        return choice


Menu.display_title(game_menu)
Menu.display_menu(game_menu)
