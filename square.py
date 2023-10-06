from enums import SquareType
from tile import ScrabbleTile

class ScrabbleSquare:
    def __init__(self, square_type: SquareType = SquareType.NO_MODIFIER, tile: ScrabbleTile = None):
        self.tile = tile
        self.square_type = square_type


    def calculate_score(self) -> tuple[int, int]:
        score = 0
        if self.tile is None:
            raise ValueError('No tile on square')
        score += self.tile.value
        multiplier = 1
        if not self.tile.placed_this_turn:
            return score, multiplier
        if self.square_type == SquareType.DOUBLE_LETTER:
            score *= 2
        elif self.square_type == SquareType.TRIPLE_LETTER:
            score *= 3
        elif self.square_type == SquareType.DOUBLE_WORD:
            multiplier *= 2
        elif self.square_type == SquareType.TRIPLE_WORD:
            multiplier *= 3
        elif self.square_type == SquareType.START:
            multiplier *= 2
        return score, multiplier


    def __repr__(self):
        return f'ScrabbleSquare({self.square_type}, {self.tile})'
    
    def __str__(self):
        if self.tile:
            return str(self.tile)
        else:
            return str(self.square_type)