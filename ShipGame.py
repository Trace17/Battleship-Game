# Author: Trace Sweeney
# GitHub Username: Trace17
# Date: Mar 01 , 2022
# Description: This class creates a Battleship game where each player has their own 10x10 grid they place their ships.
# On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to fire
# a torpedo, after which players alternate firing torpedo's. A ship is sunk when all of its squares have been hit.
# When a player sinks their opponent's final ship, they win.

class ShipGame:
    """This class creates a Battleship game where each player has their own 10x10 grid they place their ships on.
    On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to fire
    a torpedo, after which players alternate firing torpedo's. A ship is sunk when all of its squares have been hit.
    When a player sinks their opponent's final ship, they win.
    """

    def __init__(self):
        """initializes all the data members"""
        self._current_state = "UNFINISHED"
        self._player_1_spots = []
        self._first_players_ships = {}
        self._player_1_shots = []
        self._player_2_spots = []
        self._second_players_ships = {}
        self._player_2_shots = []
        self._alphabet = "ABCDEFGHIJ"
        self._players_turn = "first"

    def place_ship(self, player, ship_length, coordinates, orientation):
        """takes as a parameter the player, the ship length, the coordinates that they want the ship placed on, and
        the orientation of the ship, If a ship would not fit entirely on that player's grid, or if it would overlap
        any previously placed ships on that player's grid, or if the length of the ship is less than 2, the ship should
        not be added and the method should return False. Otherwise, the ship should be added and the method should
        return True.
        """
        if ship_length < 2:      # checks to see if the move is greater than 2
            return False
        elif orientation == "R" and int(coordinates[1]) + ship_length - 1 > 10:  # checks to see if move goes off for R
            return False
        elif orientation == "C" and ord(coordinates[0]) + ship_length - 1 > ord("J"):  # checks to see if move goes off
            return False
        else:
            list_holder = []
            if orientation == "R":
                start_length = int(coordinates[1])  # gets the start spot for the string
                end_length = int(coordinates[1]) + ship_length  # gets the end length for the placement right
                while start_length < end_length:
                    list_holder.append(coordinates[0] + str(start_length))  # puts all coordinates for spots into list
                    start_length += 1
                for spot in list_holder:  # goes through all spots in list to see if they already exist in current spots
                    if player == "first":
                        if spot in self._player_1_spots:
                            return False
                        continue
                    if player == "second":
                        if spot in self._player_2_spots:
                            return False
                        continue

            if orientation == "C":
                counter = 0
                for letter in self._alphabet:
                    counter += 1
                    if letter == coordinates[0]:  # iterates through letters in alphabet to get the number to start
                        start_length = counter - 1  # gets the start length
                        end_length = start_length + ship_length  # gets the end length
                        while start_length < end_length:
                            list_holder.append(chr(ord("A") + start_length) + coordinates[1])  # adds coordinate to list
                            start_length += 1
                        for spot in list_holder:  # goes through all spots in list to see if they exist in current spots
                            if player == "first":
                                if spot in self._player_1_spots:
                                    return False
                            if player == "second":
                                if spot in self._player_2_spots:
                                    return False
                            continue
                    continue

            if player == "first":  # if player is first, and they made a valid move then it adds the list to their spots
                self._player_1_spots += list_holder
                self._first_players_ships[coordinates] = list_holder
            else:  # if player is second, and they made a valid move then it adds the list to their spots
                self._player_2_spots += list_holder
                self._second_players_ships[coordinates] = list_holder
            return True

    def get_current_state(self):
        """returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'."""
        return self._current_state

    def fire_torpedo(self, player, coordinates):
        """ takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates of the
        target square, e.g. 'B7'. If it's not that player's turn, or if the game has already been won, it should just
        return False. Otherwise, it should record the move, update whose turn it is, update the current state (if this
        turn sank the opponent's final ship), and return True. If that player has fired on that square before,
        that's not illegal - it just wastes a turn.
        """
        if self._current_state != "UNFINISHED":
            return False
        elif self._players_turn != player:
            return False
        else:
            if player == "first":
                self._players_turn = "second"
                self._player_1_shots.append(coordinates)  # adds shot to player_1_shots (used if display method)
                for key in list(self._second_players_ships):  # iterates through the keys in the second player ships
                    temp_list = self._second_players_ships[key]  # makes a copy of the list associated with the key
                    if coordinates in temp_list:  # checks if torpedo fired hit the ship
                        temp_list.remove(coordinates)  # removes the coordinate from the list if it hit
                        self._second_players_ships[key] = temp_list  # updates the value for the key in the players dict
                        if not self._second_players_ships[key]:  # checks to see if the keys value is empty
                            del self._second_players_ships[key]  # deletes the key if it is
                        if len(self._second_players_ships) == 0:  # checks to see if the dictionary is empty
                            self._current_state = "FIRST_WON"  # if it is empty updates the current state to first won
                    continue

            if player == "second":  # same as above but for second player
                self._players_turn = "first"
                self._player_2_shots.append(coordinates)
                for key in list(self._first_players_ships):
                    temp_list = self._first_players_ships[key]
                    if coordinates in temp_list:
                        temp_list.remove(coordinates)
                        self._first_players_ships[key] = temp_list
                        if not self._first_players_ships[key]:
                            del self._first_players_ships[key]
                        if len(self._first_players_ships) == 0:
                            self._current_state = "SECOND_WON"
                    continue

            return True

    def get_num_ships_remaining(self, player):
        """takes as an argument either "first" or "second" and returns how many ships the specified player has left."""
        if player == "first":
            return len(self._first_players_ships)  # returns the length of the dictionary with the players ships
        if player == "second":
            return len(self._second_players_ships)
