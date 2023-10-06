from enum import Enum

class Direction(Enum):
    """
    Represents a direction on the Scrabble board.
    HORIZONTAL: Represents the horizontal direction.
    VERTICAL: Represents the vertical direction.
    """
    HORIZONTAL = 'h'
    VERTICAL = 'v'
    
    _opposite_mapping = {
        HORIZONTAL: VERTICAL,
        VERTICAL: HORIZONTAL
    }

    def opposite(self) -> 'Direction':
        """
        Returns the opposite direction.
        """
        return self._opposite_mapping[self]

class PlayerType(Enum):
    """
    Represents types of players in the game.
    HUMAN: Represents a human player.
    COMPUTER: Represents a computer player.
    """
    HUMAN = 1
    COMPUTER = 2

class SquareType(Enum):
    """
    Represents different types of squares on the Scrabble board with their multipliers.
    DOUBLE_LETTER: Represents a double letter score.
    TRIPLE_LETTER: Represents a triple letter score.
    DOUBLE_WORD: Represents a double word score.
    TRIPLE_WORD: Represents a triple word score.
    NO_MODIFIER: Represents a square without any score modifier.
    START: Represents the starting square.
    """
    DOUBLE_LETTER = 'DL'
    TRIPLE_LETTER = 'TL'
    DOUBLE_WORD = 'DW'
    TRIPLE_WORD = 'TW'
    NO_MODIFIER = '  '
    START = 'ST'
