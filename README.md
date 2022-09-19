# Hasami Shogi Game

Hasami Shogi using the rules for "**Variant 1**" on [the Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi), including the diagram of the starting position. Custodian captures may be made on multiple sides (up to 3 sides) of the moved piece. For example if the black piece on square h6 in the diagram below moves to square c6, then the red pieces at c4, c5, and b6 would be captured. If instead, the black piece at h6 moves to h1, then the red pieces at e1, f1, g1, and i1 would be captured.

```
  1 2 3 4 5 6 7 8 9
a . . . . . B . . .
b . . . . . R . . .
c . . B R R . . . .
d B . . . . . . . .
e R . . . . . . . .
f R . . . . . . . .
g R . . . . . . . .
h . . . . . B . . .
i R B . . . . . . .
```

Locations on the board will be specified using "algebraic notation", with rows labeled a-i and rows labeled 1-9, as shown in the diagram of the starting position shown on the Wikipedia page.

Here are some commands to run the game with:
```
game = HasamiShogiGame()              # Initializes game
game.make_move('ii', 'e1')            # Makes a move *if the move is valid*
game.print_game()                     # Prints the game board
print(game.get_active_player())       # Print the player whose turn it is (Red or Black)
print(game.get_square_occupant('a4')) # Prints the player whose piece occupies that space, or "NONE" if it is empty
print(game.get_game_state())          # Prints the current game state, either "UNFINISHED", "BLACK WON", or "RED WON"
```
