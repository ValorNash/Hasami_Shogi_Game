# Author: Valor Nash
# Date: 12/3/2021
# Description: Allows the user to play Hasami Shogi, by making movies, counting captures, removing pieces, etc.

class HasamiShogiGame:
    """The class that operates and runs the Hasami Shogi Game"""

    def __init__(self):
        """“Initializes the HasamiShogiGame Class.Takes no parameters. Initializes the board with pawns.
        Sets “counter” variable for turn to 0.
        Sets “red_captures” and “black_captures” to 0.
        All data members are private"""
        self._board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                       ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
                       ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
        self._counter = 0
        self._red_captures = 0
        self._black_captures = 0

    def print_game(self):
        """Prints the current game board"""
        for row in self._board:
            print(' '.join(map(str, row)))

    def get_game_state(self):
        """Takes no parameters. Calls get_num_captured_pieces for black. If black_captures >= 8, returns BLACK WON
        Calls get_num_captures_pieces for red. If red_captures >= 8, returns RED WON. Else, returns UNFINISHED”"""
        black = self.get_num_captured_pieces("BLACK")
        if black >= 8:
            return "BLACK WON"
        red = self.get_num_captured_pieces("RED")
        if red >= 8:
            return "RED WON"
        else:
            return "UNFINISHED"

    def get_active_player(self):
        """Takes no parameters. If “counter” is 0 or even, returns it being Black’s turn.
        If counter is odd, returns it being Red’s turn."""
        if self._counter == 0 or self._counter % 2 == 0:
            return "BLACK"
        else:
            return "RED"

    def get_num_captured_pieces(self, team):
        """Takes one parameter, red or black, and returns the number of pieces that
        color has captured by pulling either red_captures or black_captures"""
        if team in ["RED", "red", "Red"]:
            return self._red_captures
        if team in ["BLACK", "black", "Black"]:
            return self._black_captures
        else:
            return "Invalid Team Name"

    def make_move(self, current_loc, new_loc):
        """Allows the player who's turn it is to move a piece. If it is not their turn, the game is over,
        the space they chose is not occupied by their piece, the new location they chose is occupied,
        there are pieces in the way, or the move is not vertical or horizontal, will return False.
        If move is valid, sets next players turn and checks if any pieces are captured."""
        game_over = self.get_game_state()
        if game_over != "UNFINISHED":  # game is over
            return False

        check = self.get_square_occupant(current_loc)
        if check == "NONE":  # No piece at location
            return False
        curr_player = self.get_active_player()
        if check == "RED" and curr_player == "BLACK":  # Wrong player
            return False
        if check == "BLACK" and curr_player == "RED":  # Wrong player
            return False

        check_new = self.get_square_occupant(new_loc)
        if check_new != "NONE":  # New space is occupied
            return False

        col1, row1 = current_loc
        col2, row2 = new_loc
        if col1 != col2 and row1 != row2:  # Non vertical or horizontal move attempted
            return False

        if col1 == col2: # Check horizontal movement
            if row1 > row2:
                for space in range(int(row2) + 1, int(row1)):
                    next_space = (col1 + str(space))
                    is_empty = self.get_square_occupant(next_space)
                    if is_empty != "NONE":  # Piece in the way
                        return False
            if row2 > row1:
                for space in range(int(row1) + 1, int(row2)):
                    next_space = (col1 + str(space))
                    is_empty = self.get_square_occupant(next_space)
                    if is_empty != "NONE":  # Piece in the way
                        return False

        if col1 != col2: # Check vertical movement
            new_col1 = ord(col1)
            new_col2 = ord(col2)
            if col1 > col2:
                for space in range(new_col2 + 1, new_col1):
                    next_space = (chr(space) + row1)
                    is_empty = self.get_square_occupant(next_space)
                    if is_empty != "NONE":
                        return False  # Piece in the way

            if col2 > col1:
                for space in range(new_col1 + 1, new_col2):
                    next_space = (chr(space) + row1)
                    is_empty = self.get_square_occupant(next_space)
                    if is_empty != "NONE":
                        return False  # Piece in the way

        self.set_location(current_loc, ".")
        if check == "RED":  # If Red's turn, set new location to Red's Piece
            self.set_location(new_loc, "R")
        if check == "BLACK":  # If Black's turn, set new location to Black's Piece
            self.set_location(new_loc, "B")
        self.is_captured(new_loc)
        self._counter += 1  # Set next player's turn
        return True


    def get_square_occupant(self, location):
        """Takes 1 parameter, a location on the grid. If that space is R, returns RED. If that space is B,
        returns BLACK. Else, returns NONE"""
        row, col = location
        occupant = ""
        if row in ["a", "A"]:
            occupant = self._board[1][int(col)]
        if row in ["b", "B"]:
            occupant = self._board[2][int(col)]
        if row in ["c", "C"]:
            occupant = self._board[3][int(col)]
        if row in ["d", "D"]:
            occupant = self._board[4][int(col)]
        if row in ["e", "E"]:
            occupant = self._board[5][int(col)]
        if row in ["f", "F"]:
            occupant = self._board[6][int(col)]
        if row in ["g", "G"]:
            occupant = self._board[7][int(col)]
        if row in ["h", "H"]:
            occupant = self._board[8][int(col)]
        if row in ["i", "I"]:
            occupant = self._board[9][int(col)]
        if occupant == "R":
            return "RED"
        if occupant == "B":
            return "BLACK"
        else:
            return "NONE"

    def set_location(self, location, set_to):
        """Sets the specified location to a specified string. Used to move pieces around board or remove them"""
        row, col = location
        occupant = ""
        if row in ["a", "A"]:
            self._board[1][int(col)] = set_to
        if row in ["b", "B"]:
            self._board[2][int(col)] = set_to
        if row in ["c", "C"]:
            self._board[3][int(col)] = set_to
        if row in ["d", "D"]:
            self._board[4][int(col)] = set_to
        if row in ["e", "E"]:
            self._board[5][int(col)] = set_to
        if row in ["f", "F"]:
            self._board[6][int(col)] = set_to
        if row in ["g", "G"]:
            self._board[7][int(col)] = set_to
        if row in ["h", "H"]:
            self._board[8][int(col)] = set_to
        if row in ["i", "I"]:
            self._board[9][int(col)] = set_to

    def is_captured(self, new_loc):
        """Takes one parameter, new_loc, from make_move. Checks which player is making move. Checks right, left, up
        and down from new location to find if any pieces are captured, removes them from the board, and then updates
        current player's capture count."""
        player = self.get_active_player()
        col, row = new_loc
        col_num = ord(col)
        counter = 1
        # Right
        if row not in ["8", "9"]: # Makes sure it is a possible capture to the right
            next_space_r = (col + str(int(row) + counter))
            is_empty_r = self.get_square_occupant(next_space_r)
            while player != is_empty_r and is_empty_r != "NONE": # Count # of spaces being captured (if any)
                counter += 1
                next_space_r_1 = (col + str(int(row) + counter))
                is_empty_r = self.get_square_occupant(next_space_r_1)
            next_space_r_1 = (col + str(int(row) + counter))
            is_empty_r = self.get_square_occupant(next_space_r_1)
            if player == is_empty_r: # Only capture if player sandwiches
                for space in range((int(row) + 1), (int(row) + counter)):
                    next_space = (col + str(space))
                    self.set_location(next_space, ".") # Remove captured pieces
                counter -= 1
                if player == "BLACK":               # Increase # of pieces captured
                    self._black_captures += counter
                if player == "RED":
                    self._red_captures += counter

        # Left
        counter = 1 # Reset counters
        neg_counter = -1
        if row not in ["1", "2"]: # Makes sure it is a possible capture to the left
            next_space_l = (col + str(int(row) + neg_counter))
            is_empty_l = self.get_square_occupant(next_space_l)
            while player != is_empty_l and is_empty_l != "NONE": # Count # of spaces being captured (if any)
                counter += 1
                neg_counter -= 1
                next_space_l_1 = (col + str(int(row) + neg_counter))
                is_empty_l = self.get_square_occupant(next_space_l_1)
            next_space_l_1 = (col + str(int(row) + neg_counter))
            is_empty_l = self.get_square_occupant(next_space_l_1)
            if player == is_empty_l: # Only capture if player sandwiches
                for space in range((int(row) + neg_counter + 1), (int(row))):
                    next_space = (col + str(space))
                    self.set_location(next_space, ".") # Remove captured pieces
                counter -= 1
                if player == "BLACK":               # Increase # of pieces captured
                    self._black_captures += counter
                if player == "RED":
                    self._red_captures += counter

        # Up
        counter = 1 # Reset counters
        neg_counter = -1
        if col not in ["A", "a", "B", "b"]: # Makes sure it is a possible capture up
            next_space_u = (chr(col_num + neg_counter) + row)
            is_empty_u = self.get_square_occupant(next_space_u)
            while player != is_empty_u and is_empty_u != "NONE": # Count # of spaces being captured (if any)
                counter += 1
                neg_counter -= 1
                next_space_u_1 = (chr(col_num + neg_counter) + row)
                is_empty_u = self.get_square_occupant(next_space_u_1)
            next_space_u_1 = (chr(col_num + neg_counter) + row)
            is_empty_u = self.get_square_occupant(next_space_u_1)
            if player == is_empty_u: # Only capture if player sandwiches
                for space in range((col_num + neg_counter + 1), col_num):
                    next_space = (chr(space) + row)
                    self.set_location(next_space, ".") # Remove captured pieces
                counter -= 1
                if player == "BLACK":               # Increase # of pieces captured
                    self._black_captures += counter
                if player == "RED":
                    self._red_captures += counter

        # Down
        counter = 1 # Reset counters
        if col not in ["H", "h", "I", "i"]: # Makes sure it is a possible capture down
            next_space_u = (chr(col_num + counter) + row)
            is_empty_u = self.get_square_occupant(next_space_u)
            while player != is_empty_u and is_empty_u != "NONE": # Count # of spaces being captured (if any)
                counter += 1
                next_space_u_1 = (chr(col_num + counter) + row)
                is_empty_u = self.get_square_occupant(next_space_u_1)
            next_space_u_1 = (chr(col_num + counter) + row)
            is_empty_u = self.get_square_occupant(next_space_u_1)
            if player == is_empty_u: # Only capture if player sandwiches
                for space in range((col_num + 1), (col_num + counter)):
                    next_space = (chr(space) + row)
                    self.set_location(next_space, ".") # Remove captured pieces
                counter -= 1
                if player == "BLACK":               # Increase # of pieces captured
                    self._black_captures += counter
                if player == "RED":
                    self._red_captures += counter
                return


