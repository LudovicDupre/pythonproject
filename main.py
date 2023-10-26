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
cruiser = {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}
destroyer = {(5, 3): True, (6, 3): True, (7, 3): True}
submarine = {(5, 8): True, (5, 9): True, (5, 10): True}
torpedo_boat = {(9, 5): True, (9, 6): True}
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

def ask_coord():
    valid_coord = False
    shot_coord = None
    while not valid_coord:
        player_coord = input("Entrez les coordonnées de votre tir (ex. : 'A1', 'H8') : ")
        if 2 <= len(player_coord) <= 3:
            letter, number = player_coord[0], player_coord[1:]
            letter = letter.upper()
            try:
                line_no = int(number)
                column_no = ord(letter) - ord('A') + 1
                if 1 <= line_no <= GRID_SIZE and letter in LETTERS:
                    valid_coord = True
                    shot_coord = (line_no, column_no)
            except ValueError:
                pass
    return shot_coord

def ship_is_hit(ship, shot_coord):
    if shot_coord in ship:
        print('Un navire a été touché par votre tir !')
        ship[shot_coord] = False
        if all(val is False for val in ship.values()):
            print('Le navire touché est coulé !!')
            ships_list.remove(ship)
    else:
        print("Votre tir est tombé dans l'eau")

def analyze_shot(ship, shot_coord):
    if shot_coord in ship:
        print('Un navire a été touché par votre tir !')
        ship[shot_coord] = False
        if all(val is False for val in ship.values()):
            print('Le navire touché est coulé !!')
            ships_list.remove(ship)
        return True
    else:
        print("Votre tir est tombé dans l'eau")
        return False

def play_battleship():
    while ships_list:
        shot_coord = ask_coord()
        for ship in ships_list:
            if analyze_shot(ship, shot_coord):
                break

    print('Bravo, vous avez coulé tous les navires')

if __name__ == "__main__":
    play_battleship()
