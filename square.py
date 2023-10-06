from enums import SquareType
from exceptions import NoTileError, TilePlacementError
from tile import ScrabbleTile

class ScrabbleSquare:
    def __init__(self, square_type: SquareType = SquareType.NO_MODIFIER, tile: ScrabbleTile = None):
        self._tile: ScrabbleTile = tile
        self.square_type: SquareType = square_type

    @property
    def tile(self) -> ScrabbleTile:
        return self._tile
    
    @tile.setter
    def tile(self, new_tile: ScrabbleTile):
        if self._tile is not None:
            raise TilePlacementError("This square is already occupied by a tile.")
        self._tile = new_tile

    def calculate_score(self) -> tuple[int, int]:
        if self.tile is None:
            raise NoTileError('No tile on square')

        score = self.tile.value
        multiplier = 1

        if self.tile.placed_this_turn:
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

    def remove_tile(self) -> ScrabbleTile:
        """Removes and returns the tile from the square. If no tile is present, raises an error."""
        if not self.tile:
            raise NoTileError("No tile on the square to remove.")
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