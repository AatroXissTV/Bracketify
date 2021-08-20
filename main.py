# Entry point
import exceptions as exc

players = list()  # global variables where we keep data


def create_player(pseudo, gender, ranking):
    global players
    results = list(filter(lambda x: x['pseudo'] == pseudo, players))
    if results:
        raise exc.PlayerAlreadyExisting('"{}" already stored'.format(players))
    else:
        players.append({
            'pseudo': pseudo,
            'gender': gender,
            'ranking': ranking,
            })


def create_players(app_players):
    global players
    players = app_players


def read_player(pseudo):
    global players
    myplayers = list(filter(lambda x: x['pseudo'] == pseudo, players))
    if myplayers:
        return myplayers[0]
    else:
        raise exc.PlayerNotExisting(
            'Can\'t read "{}" because it\'s not stored'.format(pseudo)
        )


def read_players():
    global players
    return [player for player in players]


def update_player(pseudo, gender, ranking):
    global players
    pdxs_players = list(
        filter(lambda p_x: p_x[1]['pseudo'] == pseudo, enumerate(players))
    )
    if pdxs_players:
        p, player_to_update = pdxs_players[0][0], pdxs_players[0][1]
        players[p] = {'pseudo': pseudo, 'gender': gender, 'ranking': ranking}
    else:
        raise exc.PlayerNotExisting(
            'Can\'t update "{}" because it\'s not stored'.format(pseudo)
        )


def delete_player(pseudo):
    global players
    pdxs_players = list(
        filter(lambda p_x: p_x[1]['pseudo'] == pseudo, enumerate(players))
    )
    if pdxs_players:
        p, player_to_delete = pdxs_players[0][0], pdxs_players[0][1]
        del players[p]
    else:
        raise exc.PlayerNotExisting(
            'Can\'t update "{}" because it\'s not stored'.format(pseudo)
        )


def main():

    my_items = [
        {'pseudo': 'Zerator', 'gender': 'M', 'ranking': 1},
        {'pseudo': 'LittleBigWhale', 'gender': 'M', 'ranking': 2},
        {'pseudo': 'Apaxo', 'gender': 'F', 'ranking': 3},
        ]

    # CREATE
    # If we try to re-create an object we get PlayerAlreadyExisting exception
    create_players(my_items)
    # Create a new player
    create_player('Mynthos', gender='M', ranking=4)

    # READ
    print("-----------------")
    print('READ players')
    # If we try to read an object we get an PlayerNotExisting exception
    print(read_players())
    print("-----------------")
    print("-----------------")
    print('READ Zerator')
    print(read_player('Zerator'))
    print("-----------------")

    # UPDATE
    print("-----------------")
    print('UPDATE LittleBigWhale')
    update_player('LittleBigWhale', gender='F', ranking=2)
    print(read_player('LittleBigWhale'))
    print("-----------------")

    # DELETE
    print("-----------------")
    print('DELETE Apaxo')
    delete_player('Apaxo')
    print("-----------------")

    print("-----------------")
    print('READ players')
    print(read_players())
    print("-----------------")


if __name__ == '__main__':
    main()
