from copy import deepcopy

from board import ScrabbleBoard
from enums import Direction, SquareType
from settings_manager import SettingsManager
from player import Player
from exceptions import InvalidWordError, InvalidPlacementError, TilesNotConnectedError, InsufficientTilesError
from word import Word

class Move:
    def __init__(self, row: int, col: int, word: str, direction: Direction, 
                 player: Player):
        self.row = row
        self.col = col
        self.word = word
        self.direction = direction
        self.player = player
        self.connected = False 
        self.valid_move = False

    def execute(self, board: ScrabbleBoard, settings_manager: SettingsManager):
        self.validate_move(board, settings_manager)
        self.apply_move(board, settings_manager)


    def validate_move(self, board: ScrabbleBoard, settings_manager: SettingsManager) -> None:
        """Validate that the word can be placed at the specified location and direction on the board."""
        if not settings_manager.is_valid_word(self.word):
            raise InvalidWordError('Invalid word')
        offset_r = (self.direction == Direction.VERTICAL)
        offset_c = (self.direction == Direction.HORIZONTAL)
        modifiable_player = deepcopy(self.player)
        modifiable_board = deepcopy(board)
        
        for index, char in enumerate(self.word):
            r_offset = (index * offset_r)
            c_offset = (index * offset_c)
            square = modifiable_board.get_square(self.row + r_offset, self.col + c_offset)
            if square.tile is not None:
                if square.tile != char:
                    raise InvalidPlacementError('Invalid placement')
                self.connected = True
            else:
                tile = modifiable_player.rack.get_tile(char)
                if tile is None:
                    raise InsufficientTilesError('Insufficient tiles')
                if square.square_type == SquareType.START:
                    self.connected = True
                square.tile = tile
                self.check_normal_words(self.row + r_offset, self.col + c_offset, self.direction, modifiable_board, settings_manager, False)
        if not self.connected:
            raise TilesNotConnectedError('Tiles not connected')                
        self.valid_move = True

    def calculate_score(self, board: ScrabbleBoard, settings_manager: SettingsManager) -> int:
        total_score = 0
        word_multiplier = 1

        current_row = self.row
        current_col = self.col
        for letter in self.word:
            current_square = board.get_square(current_row, current_col)
            tile_score_modifier, tile_multiplier_modifier = current_square.calculate_score()
            total_score += tile_score_modifier
            word_multiplier *= tile_multiplier_modifier
            if current_square.tile.placed_this_turn:
                self.check_normal_words(current_row, current_col, self.direction, board, settings_manager)

            current_row += (self.direction == Direction.VERTICAL)
            current_col += (self.direction == Direction.HORIZONTAL)
        
        total_score *= word_multiplier

        if len(self.word) == settings_manager.game_mechanics.max_rack_size:
            total_score += settings_manager.game_mechanics.bingo_bonus

        return total_score
    
    def apply_move(self, board: ScrabbleBoard, settings_manager: SettingsManager):
        current_row = self.row
        current_col = self.col
        placed_tiles = []
        for letter in self.word:
            current_square = board.get_square(current_row, current_col)
            if current_square.tile is None:
                tile = self.player.rack.get_tile(letter)
                tile.placed_this_turn = True
                placed_tiles.append(tile)
                current_square.tile = tile
                self.player.rack.remove_tile(tile)
            
            current_row += (self.direction == Direction.VERTICAL)
            current_col += (self.direction == Direction.HORIZONTAL)
        
        self.player.score += self.calculate_score(board, settings_manager)
        for tile in placed_tiles:
            tile.placed_this_turn = False

    def check_normal_words(self, row: int, col: int, direction: Direction, board: ScrabbleBoard, 
                           settings_manager: SettingsManager, modify_score: bool = True) -> None:

        for delta in [-1, 1]:
            r_offset = delta if direction == Direction.HORIZONTAL else 0
            c_offset = delta if direction == Direction.VERTICAL else 0
            if board.get_square(row + r_offset, col + c_offset).tile:
                word = Word(row + r_offset, col + c_offset, direction.opposite(), board, settings_manager)
                self.connected = True
                self.player.score += word.calculate_score(board) * (modify_score)