from copy import deepcopy

from board import ScrabbleBoard
from player import Player
from enums import Direction
from word import Word
from settings_manager import SettingsManager
from enums import SquareType
from tile import ScrabbleTile

class Move:
    def __init__(self, row: int, col: int, word: str, direction: Direction, 
                 player: Player):
        self.row = row
        self.col = col
        self.word = word
        self.direction = direction
        self.player = player

    def execute(self, board: ScrabbleBoard, settingsManager: SettingsManager):
        current_board, settingsManager, current_player = self.simulate_move(board, settingsManager)

        board.board = current_board.board
        self.player.rack = current_player.rack
        self.player.score = current_player.score

    def validate_move(self, board: ScrabbleBoard, settingsManager: SettingsManager):
        if not settingsManager.is_valid_word(self.word):
            raise ValueError('Invalid word')
        board.validate_move(self.row, self.col, self.word, self.direction)

    def simulate_move(self, board: ScrabbleBoard, settingsManager: SettingsManager):
        current_board = deepcopy(board)
        current_settings_manager = deepcopy(settingsManager)
        current_player = deepcopy(self.player)
        placed_tiles = []

        current_row = self.row
        current_col = self.col
        word_score = 0
        word_multiplier = 1
        for letter in self.word:
            current_square = current_board.get_square(current_row, current_col)
            if current_square.tile is None:
                tile: ScrabbleTile = current_player.rack.get_tile(letter)
                if tile is None:
                    raise ValueError('Invalid tiles')
                if current_square.square_type == SquareType.START:
                    self.connected = True
                current_square.tile = tile
                current_square.tile.placed_this_turn = True
                placed_tiles.append(current_square.tile)
                current_player.rack.remove_tile(tile)
                self.check_normal_words(current_row, (self.direction == Direction.HORIZONTAL), 
                                        current_col, (self.direction == Direction.VERTICAL), 
                                        self.direction, current_board, current_settings_manager,
                                        current_player)
            else:
                if current_square.tile != letter:
                    raise ValueError('Invalid placement')
                self.connected = True
                
            word_score_modifier, word_multiplier_modifier = current_square.calculate_score()
            word_score += word_score_modifier
            word_multiplier *= word_multiplier_modifier
            
            current_row += (self.direction == Direction.VERTICAL)
            current_col += (self.direction == Direction.HORIZONTAL)

        if len(placed_tiles) == current_settings_manager.max_rack_size:
            current_player.score += current_settings_manager.bingo_bonus
        
        for tile in placed_tiles:
            tile.placed_this_turn = False
        current_player.score += word_score * word_multiplier 
        if not self.connected:
            raise ValueError('Invalid placement')        
        return current_board, current_settings_manager, current_player
    
    def check_normal_words(self, row: int, row_delta: int, col: int, col_delta: int, direction: Direction, board: ScrabbleBoard, settingsManager: SettingsManager, current_player: Player):
        if board.get_square(row + row_delta, col + col_delta).tile is not None:
            try:
                word = Word(row + row_delta, col + col_delta, direction.opposite(), board, settingsManager)
            except ValueError:
                raise ValueError('Invalid normal word at ' + str(row) + ', ' + str(col) + ' ' + word.word)
            self.connected = True
            current_player.score += word.calculate_score(board)
        if board.get_square(row - row_delta, col - col_delta).tile is not None:
            try:
                word = Word(row - row_delta, col - col_delta, direction.opposite(), board, settingsManager)
            except ValueError:
                raise ValueError('Invalid normal word at ' + str(row) + ', ' + str(col) + ' ' + word.word)
            self.connected = True
            current_player.score += word.calculate_score(board)