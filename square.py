from typing import Optional
from enums import SquareType
from exceptions import SquareOccupiedError, NoTileError
from tile import ScrabbleTile



class ScrabbleSquare:
    def __init__(self, square_type: SquareType = SquareType.NO_MODIFIER, tile: Optional[ScrabbleTile] = None):
        self._tile: ScrabbleTile = tile
        self._square_type: SquareType = square_type

    @property
    def tile(self) -> ScrabbleTile:
        return self._tile
    
    @tile.setter
    def tile(self, new_tile: ScrabbleTile) -> None:
        if self._tile is not None:
            raise SquareOccupiedError()
        self._tile = new_tile

    @property
    def square_type(self) -> SquareType:
        """Return the type of the square."""
        return self._square_type


    @property
    def square_type(self) -> SquareType:
        """Return the type of the square."""
        return self._square_type

    def calculate_score(self) -> int:
        """Calculate and return the score of the tile considering the square type."""
        if self.tile is None:
            raise NoTileError()

        score = self.tile.value
        multiplier = 1

        if self.tile.placed_this_turn:
            if self._square_type == SquareType.DOUBLE_LETTER:
                score *= 2
            elif self._square_type == SquareType.TRIPLE_LETTER:
                score *= 3
            elif self._square_type in [SquareType.DOUBLE_WORD, SquareType.START]:
                multiplier *= 2
            elif self._square_type == SquareType.TRIPLE_WORD:
                multiplier *= 3

        return score, multiplier

    def remove_tile(self) -> ScrabbleTile:
        """Removes and returns the tile from the square. If no tile is present, raises an error."""
        if not self.tile:
            raise NoTileError()
        removed_tile = self._tile
        self._tile = None
        return removed_tile
    
    def __repr__(self) -> str:
        return f'ScrabbleSquare({self.square_type}, {self.tile})'
    
    def __str__(self) -> str:
        if self.tile:
            return str(self.tile)
        else:
            return str(self.square_type)
