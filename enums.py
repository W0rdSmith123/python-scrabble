from enum import Enum

class Direction(Enum):
    HORIZONTAL = 'h'
    VERTICAL = 'v'

    def opposite(self):
        if self == Direction.HORIZONTAL:
            return Direction.VERTICAL
        elif self == Direction.VERTICAL:
            return Direction.HORIZONTAL

class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2

class SquareType(Enum):
    DOUBLE_LETTER = 'DL'
    TRIPLE_LETTER = 'TL'
    DOUBLE_WORD = 'DW'
    TRIPLE_WORD = 'TW'
    NO_MODIFIER = '  '
    START = 'ST'

    def __repr__(self):
        return f'Multiplier.{self.name}'

    def __str__(self):
        return self.value
