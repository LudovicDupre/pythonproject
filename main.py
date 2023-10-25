#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées, un tuple (no_ligne, no_colonne)
# un no_ligne ou no_colonne est compris dans le programme entre 1 et 10,
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')

GRID_SIZE = 10

# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTERS = "ABCDEFGHIJ"

# chaque navire est constitué d'un dictionnaire dont les clés sont les
# coordonnées de chaque case le composant, et les valeurs correspondantes
# l'état de la partie du navire correspondant à la case
# (True : intact ; False : touché)

# les navires suivants sont disposés de façon fixe dans la grille :
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | o | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  9 |   |   |   |   | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# | 10 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
aircraft_carrier = {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}
cruiser          = {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}
destroyer        = {(5, 3): True, (6, 3): True, (7, 3): True}
submarine        = {(5, 8): True, (5, 9): True, (5, 10): True}
torpedo_boat     = {(9, 5): True, (9, 6): True}
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# l'embryon de notre jeu consiste à demander à l'infini au joueur les coordonnées
# d'un tir, puis à indiquer si ce tir touche un navire (en mémorisant les conséquences
# de ce tir, indiquant si le navire est coulé à la suite de plusieurs tirs convergents,
# et si la partie est finie lorsque le dernier navire est coulé)
while ships_list:

    # on demande des coordonnées au joueur tant qu'il n'en fournit pas de valides
    # (ex. : 'A1', 'H8'), puis on les transforme en des coordonnées du programme :
    # tuple (no_ligne, no_colonne)
    valid_coord = False
    shot_coord = None  # pour éviter un avertissement ("can be undefined")
    while not valid_coord:

        # ex. d'entrée attendue : 'A1'
        player_coord = input("Entrez les coordonnées de votre tir (ex. : 'A1', 'H8') : ")

        if 2 <= len(player_coord) <= 3:
            letter, number = player_coord[0], player_coord[1:]
            letter = letter.upper()
            try:
                # détermination de line_no et column_no (comptés à partir de 1)
                line_no = int(number)
                column_no = ord(letter) - ord('A') + 1
                if 1 <= line_no <= GRID_SIZE and letter in LETTERS:
                    valid_coord = True
                    shot_coord = (line_no, column_no)
            except ValueError:
                pass

    # on regarde à présent si le tir en coord_tir touche un navire
    for ship in ships_list:
        if shot_coord in ship:
            print('Un navire a été touché par votre tir !')
            # on mémorise ce tir
            ship[shot_coord] = False
            # on regarde si le navire est coulé
            if True not in ship.values():
                print('Le navire touché est coulé !!')
                # le navire est supprimé de la flotte
                ships_list.remove(ship)
            break
    else:
        print("Votre tir est tombé dans l'eau")

print('Bravo, vous avez coulé tous les navires')
