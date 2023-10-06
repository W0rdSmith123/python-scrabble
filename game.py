from typing import Optional, Set

from settings_manager import SettingsManager
from board import ScrabbleBoard
from bag import ScrabbleBag
from player import Player
from enums import Direction
from move import Move

class Game:
    def __init__(self, word_set: Set[str], settings_dict: Optional[dict] = None, player_names: Optional[list[str]] = None):
        # Load settings from settings.json
        self.settings_manager = SettingsManager(word_set, settings_dict)
        if player_names is None:
            player_names = range(1, self.settings_manager.player_count + 1) 
        if len(player_names) != self.settings_manager.game_mechanics.player_count:
            raise IndexError('Number of player names does not match number of players.')
        # Initialize board, bag, and players
        self.board = ScrabbleBoard(self.settings_manager.board_settings.default_board_layout)
        self.bag = ScrabbleBag(self.settings_manager)

        if len(self.bag) < self.settings_manager.game_mechanics.max_rack_size * self.settings_manager.game_mechanics.player_count:
            raise IndexError('Tile distribution is not large enough for the number of players.')
        self.players: list[Player] = []
        for player_name in player_names:
            self.players.append(Player((player_name), self.bag, self.settings_manager))
        self.players.sort()

        # Initialize game variables
        self.current_player = self.players[0]
        self.zero_score_streak: int = 0
        self.is_over: bool = self.has_ended()

    def has_ended(self) -> bool:
        if any([
            self.zero_score_streak >= self.settings_manager.game_mechanics.zero_score_turns_before_game_end,
            len(self.players) == 1,
            any(len(player.rack) == 0 for player in self.players)
        ]):
            return True
        return False

    def _rotate_to_next_player(self):
        """Select the next player in the rotation."""
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % len(self.players)
        self.current_player = self.players[next_index]

    def _end_turn_operations(self):
        """Operations to be performed at the end of every turn."""
        self._rotate_to_next_player()
        self.is_over = self.has_ended()

    def make_move(self, row: int, col: int, word: str, direction: Direction, current_player: Player = None):
        current_player = current_player or self.current_player
        old_player_score = current_player.score

        move = Move(row, col, word, direction, current_player)
        move.validate_move(self.board, self.settings_manager)
        move.execute(self.board, self.settings_manager)

        current_player.rack.refill(self.bag)
        if current_player.score == old_player_score:
            self.zero_score_streak += 1
        else:
            self.zero_score_streak = 0
        self._end_turn_operations()

    def exchange_tiles(self, tiles: str, current_player: Player = None):
        current_player = current_player or self.current_player
        current_player.exchange_tiles(tiles, self.bag, self.settings_manager)
        self.zero_score_streak += 1
        self._end_turn_operations()

       
    def pass_turn(self, current_player: Player = None):
        current_player = current_player or self.current_player
        self.zero_score_streak += 1
        self._end_turn_operations()

    def resign(self, current_player: Player = None):
        current_player = current_player or self.current_player
        self.players.remove(current_player)
        self.current_player = self.players[0]
        self.is_over = self.has_ended()

    def apply_end_game_penalties(self) -> None:
        for player in self.players:
            for tile in player.rack:
                player.score -= tile.value
    
    def __str__(self):
        current_player = self.current_player
        output = ''
        output += f'{current_player.name}\'s turn\n'
        output += f'Current score: {current_player.score}\n'
        output += f'Current rack: {current_player.rack}\n'
        output += str(self.board)
        output += f'Tiles remaining: {len(self.bag)}'
        return output