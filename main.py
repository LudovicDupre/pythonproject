#!/usr/bin/env python
#  -*- coding: utf-8 -*-

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.coordinates = []

    def place_ship(self, x, y, orientation):
        if orientation == "horizontal":
            for i in range(self.length):
                self.coordinates.append((x + i, y))
        elif orientation == "vertical":
            for i in range(self.length):
                self.coordinates.append((x, y + i))

    def is_hit(self, x, y):
        return (x, y) in self.coordinates

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def display(self):
        print("  A B C D E F G H I J")
        for i in range(self.size):
            row = ' '.join(self.grid[i])
            print(f"{i+1} {row}")

    def place_ship(self, ship, x, y, orientation):
        if self.is_valid_placement(ship, x, y, orientation):
            ship.place_ship(x, y, orientation)
            self.ships.append(ship)
            for coord in ship.coordinates:
                x, y = coord
                self.grid[y][x] = "O"
            return True
        return False

    def is_valid_placement(self, ship, x, y, orientation):
        if (x < 0 or y < 0 or x >= self.size or y >= self.size):
            return False
        if orientation == "horizontal":
            if x + ship.length > self.size:
                return False
            for i in range(ship.length):
                if self.grid[y][x + i] == "O":
                    return False
        elif orientation == "vertical":
            if y + ship.length > self.size:
                return False
            for i in range(ship.length):
                if self.grid[y + i][x] == "O":
                    return False
        return True

    def is_all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

    def play_shot(self, x, y):
        if (x < 0 or y < 0 or x >= self.size or y >= self.size):
            return False
        if self.grid[y][x] == "O":
            for ship in self.ships:
                if ship.is_hit(x, y):
                    self.grid[y][x] = "X"
                    print("Hit!")
                    if ship.is_sunk():
                        print(f"{ship.name} has been sunk!")
                    return True
        else:
            self.grid[y][x] = "."
            print("Miss!")
            return False

    @staticmethod
    def ask_coord():
        while True:
            try:
                coord = input("Enter target coordinates (e.g., A1): ").strip().upper()
                if len(coord) == 2 and 'A' <= coord[0] <= 'J' and '1' <= coord[1] <= '10':
                    x = ord(coord[0]) - ord('A')
                    y = int(coord[1]) - 1
                    return x, y
                else:
                    print("Invalid coordinates. Please try again.")
            except ValueError:
                print("Invalid coordinates. Please try again.")

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

ships_list = []
aircraft_carrier = Ship('porte_avion',
                        {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True},
                        ships_list)
cruiser          = Ship('croiseur',
                        {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True},
                        ships_list)
destroyer        = Ship('contre torpilleur',
                        {(5, 3): True, (6, 3): True, (7, 3): True},
                        ships_list)
submarine        = Ship('sous-marin',
                        {(5, 8): True, (5, 9): True, (5, 10): True},
                        ships_list)
torpedo_boat     = Ship('torpilleur',
                        {(9, 5): True, (9, 6): True},
                        ships_list)

# -------------------------------------------------------------------------- #
# programme principal :                                                      #
# tant que tous les navires ne sont pas coulés, on demande au joueur         #
# d'indiquer une case où il souhaite effectuer un tir                         #
# -------------------------------------------------------------------------- #

grid = Grid(ships_list)
while ships_list:
    grid.display()
    next_shot_coord = Grid.ask_coord()
    grid.play_shot(next_shot_coord)

grid.display()
print('Bravo, vous avez coulé tous les navires')
