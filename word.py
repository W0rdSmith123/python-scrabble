from enums import Direction
from settings_manager import SettingsManager
from board import ScrabbleBoard
from exceptions import InvalidWordError

class Word:
    def __init__(self, row: int, column: int, direction: Direction, board: ScrabbleBoard, settings_manager: SettingsManager):
        """Initializes a Word instance using the starting position and the board."""
        self.row = row
        self.column = column
        self.direction = direction
        self.word = ''
        self.score = 0
        self.multiplier = 1
        self.calculate_word(board, settings_manager)

    def find_starting_point(self, board: ScrabbleBoard) -> None:
        """Finds and sets the starting position of the word."""
        row_offset = self.direction == Direction.VERTICAL
        col_offset = self.direction == Direction.HORIZONTAL

        while board.get_square(self.row - row_offset, self.column - col_offset).tile:
            if row_offset:
                self.row -= 1
            if col_offset:
                self.column -= 1

    def construct_word(self, board: ScrabbleBoard) -> None:
        """Constructs the word based on the starting position and direction."""
        self.word = ''
        offset = 0
        row_offset = (self.direction == Direction.VERTICAL)
        col_offset = (self.direction == Direction.HORIZONTAL)

        current_square = board.get_square(self.row + row_offset * offset, self.column + col_offset * offset)
        while current_square.tile:
            self.word += current_square.tile.letter
            offset += 1
            current_square = board.get_square(self.row + row_offset * offset, self.column + col_offset * offset)
        self.word = self.word.upper()

    def calculate_word(self, board: ScrabbleBoard, settings_manager: SettingsManager) -> None:
        """Validates and constructs the word from the board."""
        self.find_starting_point(board)
        self.construct_word(board)
        if not settings_manager.is_valid_word(self.word):
            raise InvalidWordError(f'Invalid word: {self.word}')

    def calculate_score(self, board: ScrabbleBoard) -> int:
        """Calculates and returns the score of the word."""
        self.score = 0
        self.multiplier = 1
        current_row = self.row
        current_column = self.column

        for _ in self.word:
            square = board.get_square(current_row, current_column)
            tile_score, tile_multiplier = square.calculate_score()
            self.score += tile_score
            self.multiplier *= tile_multiplier
            if self.direction == Direction.HORIZONTAL:
                current_column += 1
            else:
                current_row += 1

        self.score *= self.multiplier
        return self.score
