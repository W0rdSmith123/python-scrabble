from enum import Enum

class Direction(Enum):
    HORIZONTAL = 'h'
    VERTICAL = 'v'

    @classmethod
    def _get_opposite_mapping(cls):
        return {
            cls.HORIZONTAL: cls.VERTICAL,
            cls.VERTICAL: cls.HORIZONTAL
        }

    def opposite(self) -> 'Direction':
        opposite_mapping = self._get_opposite_mapping()
        return opposite_mapping[self]
    
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

    def __str__(self) -> str:
        return self.value