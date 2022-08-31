# Battleship-Game
This program creates a Battleship game where each player has their own 10x10 grid they place their ships. On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to fire a torpedo, after which players alternate firing torpedo's. A ship is sunk when all of its squares have been hit. When a player sinks their opponent's final ship, they win.

## How to use it
To use this program download the "ShipGame.py" file, start a game by entering "game = ShipGame()" and begin placing ships by entering "game.place_ship('first', 5, 'B2', 'C')" where 'first' represents the first player, 'second' represents the second player, 5 represents the length of the ship being placed and 'B2' represents the spot you are placing the ship, lastly 'C' represents column for the orientation of the ship, users can also enter 'R' for Row. Valid coordinates are between letters A-J and numbers 0-9. To fire a torpedo a user would enter "game.fire_torpedo('first', 'H3')" where 'first' represents the player and 'H3' the coordinates the user is firing the torpedo at. Users can check the states of the game by calling "print(game.get_current_state())" and get the number of ships remaining by calling "print(game.get_num_ships_remaining())"

Example:
game = ShipGame()
game.place_ship('first', 5, 'B2', 'C')
game.place_ship('first', 2, 'I8', 'R')
game.place_ship('second', 3, 'H2, 'C')
game.place_ship('second', 2, 'A1', 'C')
game.place_ship('first', 8, 'H2', 'R')
game.fire_torpedo('first', 'H3')
game.fire_torpedo('second', 'A1')
print(game.get_current_state())
