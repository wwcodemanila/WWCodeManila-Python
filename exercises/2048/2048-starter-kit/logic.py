""" Clone of 2048 game.
Credit to:
    http://flothesof.github.io/2048-game.html
    https://github.com/enixdark/principlescomputing-001/tree/master/Week0

Game instruction:
    https://github.com/enixdark/principlescomputing-001/blob/master/Week0/Instructions.md
To run:
    python logic.py
"""
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {
    UP: (1, 0),
    DOWN: (-1, 0),
    LEFT: (0, 1),
    RIGHT: (0, -1)
}

# Symbol for an empty tile, DO NOT MODIFY
EMPTY_TILE = 0


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    Example:
        [2 0 2 2] ->  [4 2 0 0]
        [0 2 2 0] -> [4 0 0 0]
        [2 2 2 8] -> [4 2 8 0]
        [0 2 2 4] -> [4 4 0 0]
        [2 2 2 2] -> [4 4 0 0]
        [256 256   2   4] -> [512   2   4   0]
        [256 128  64  32] -> [256 128  64  32]
        [2 0 2 0] -> [4 0 0 0]
        [2 0 2 4] -> [4 4 0 0]
        [0 0 2 2] -> [4 0 0 0]
        [8 16 16 8] -> [8 32 8 0]
    """
    # replace with your code (Phase 1)
    return []


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height=4, grid_width=4):
        # Store the board's height (Phase 2)

        # Store the board's width (Phase 2)

        # Store each direction's initial indices (Phase 3)

        # Initialize your board (Phase 2)
        pass

    def __str__(self):
        """
        Returns a string representation of the board for debugging.
        """
        # replace with your code (Phase 2)
        return ""

    def reset(self):
        """
        Reset the game so the board is empty except for two
        initial tiles.
        """
        # Initialize your height * width board with empty tiles (Phase 2)

        # Create two new tiles (Phase 3)
        pass

    def get_grid_height(self):
        """
        Returns the height of the board.
        """
        # replace with your code (Phase 2)
        return 0

    def get_grid_width(self):
        """
        Returns the width of the board.
        """
        # replace with your code (Phase 2)
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code (Phase 3)
        pass

    def new_tile(self):
        """
        Creates a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code (Phase 3)

        # Bonus: Check if board is full and do not generate new tile

        # Generate a random number up to 1

        # Assign new tile depending on generated number

        # Place new tile on randomly selected empty square from board
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code (Phase 2)
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code (Phase 2)
        return 0


game = TwentyFortyEight()

# Try to show your board
# print(game)

# It is advisable to use the GUI once you are in Phase 3
# poc_2048_gui.run_gui(TwentyFortyEight())
