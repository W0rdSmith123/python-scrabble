from enums import Direction
from settings_manager import SettingsManager
from board import ScrabbleBoard

class Word:
    def __init__(self, row: int, column: int, direction: Direction, board: ScrabbleBoard, settingsManager: SettingsManager):
        self.row = row
        self.column = column
        self.direction = direction
        self.word = ''
        self.calculate_word(board, settingsManager)

    def find_starting_point(self, board: ScrabbleBoard):
        offset = 0
        while board.get_square(self.row     - (self.direction == Direction.VERTICAL) * offset, self.column - (self.direction == Direction.HORIZONTAL) * offset).tile is not None:
            offset += 1
        offset -= 1
        self.row = self.row - (self.direction == Direction.VERTICAL) * offset
        self.column = self.column - (self.direction == Direction.HORIZONTAL) * offset
    
    def construct_word(self, board: ScrabbleBoard):
        self.word = ''
        current_square = board.get_square(self.row, self.column)
        offset = 0
        while current_square.tile is not None:
            self.word += current_square.tile.letter
            offset += 1
            current_square = board.get_square(self.row + (self.direction == Direction.VERTICAL) * offset, self.column + (self.direction == Direction.HORIZONTAL) * offset)
        self.word = self.word.upper()       
    def calculate_word(self, board: ScrabbleBoard, settingsManager: SettingsManager):
        self.find_starting_point(board)
        self.construct_word(board)
        if not settingsManager.is_valid_word(self.word):
            raise ValueError('Invalid word')

    def calculate_score(self, board: ScrabbleBoard):
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
            elif self.direction == Direction.VERTICAL:
                current_row += 1
        self.score *= self.multiplier
        return self.score