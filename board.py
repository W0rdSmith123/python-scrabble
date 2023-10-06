from typing import List

from enums import Direction, SquareType
from exceptions import InvalidMoveError, OutOfBoundsError
from square import ScrabbleSquare

class ScrabbleBoard:
    """
    Represents a Scrabble game board.
    Allows retrieving and validating squares based on row and column.
    """

    def __init__(self, default_board_layout: List[List[str]]):
        self._board = [[ScrabbleSquare(SquareType(square)) for square in row] for row in default_board_layout]

    def get_square(self, row: int, col: int) -> ScrabbleSquare:
        """Get the square at the specified row and column."""
        if 0 <= row < len(self._board) and 0 <= col < len(self._board[0]):
            return self._board[row][col]
        raise OutOfBoundsError('Row or column out of bounds')

    def validate_move(self, row: int, col: int, word: str, direction: Direction) -> None:
        """Validate that the word can be placed at the specified location and direction on the board."""
        for i in range(len(word)):
            r_offset = i if direction == Direction.VERTICAL else 0
            c_offset = i if direction == Direction.HORIZONTAL else 0
            if row + r_offset >= len(self._board) or col + c_offset >= len(self._board[0]):
                raise InvalidMoveError('Word does not fit on the board in the given direction')
            self.get_square(row + r_offset, col + c_offset)

    @property
    def board(self) -> List[List[ScrabbleSquare]]:
        """Get a copy of the board without allowing modification to the original board."""
        return [row.copy() for row in self._board]

    @board.setter
    def board(self, new_board: List[List[ScrabbleSquare]]) -> None:
        """Set the board to a new board."""
        self._board = new_board
        
    def __repr__(self):
        return f'ScrabbleBoard(rows={len(self._board)}, cols={len(self._board[0])})'

    def __str__(self):
        headers = '   ' + ' '.join([f'{i:2}' for i in range(len(self._board[0]))])
        border = '   ' + '+--' * len(self._board[0]) + '+'
        rows = [
            f'{i:2} |' + '|'.join([str(square) for square in row]) + '|'
            for i, row in enumerate(self._board)
        ]
        return '\n'.join([headers, border] + [val for pair in zip(rows, [border] * len(rows)) for val in pair])

    def __getitem__(self, index: int) -> List[ScrabbleSquare]:
        """Allow indexing to retrieve rows."""
        return self._board[index]
