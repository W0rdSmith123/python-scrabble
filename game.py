from settings_manager import SettingsManager
from board import ScrabbleBoard
from bag import ScrabbleBag
from player import Player
from enums import Direction
from move import Move

class Game:
    def __init__(self, path_to_settings_json: str, player_names: list[str] = None):
        # Load settings from settings.json
        self.settings_manager = SettingsManager(path_to_settings_json)
        if player_names is None:
            player_names = range(1, self.settings_manager.player_count + 1) 
        if len(player_names) != self.settings_manager.player_count:
            raise IndexError('Number of player names does not match number of players.')
        # Initialize board, bag, and players
        self.board = ScrabbleBoard(self.settings_manager.default_board_layout)
        self.bag = ScrabbleBag(self.settings_manager.tile_distribution, self.settings_manager.letter_scores)
        if len(self.bag) < self.settings_manager.max_rack_size * self.settings_manager.player_count:
            raise IndexError('Tile distribution is not large enough for the number of players.')
        # Initialize players
        self.players: list[Player] = []
        for player_name in player_names:
            self.players.append(Player((player_name), self.bag, self.settings_manager))
        self.players.sort()

        # Initialize game variables
        self.current_player = self.players[0]
        self.zero_score_streak: int = 0
        self.is_over: bool = self.has_ended()

    def has_ended(self) -> bool:
        if len(self.bag) == 0:
            return True
        if self.zero_score_streak >= self.settings_manager.zero_score_turns_before_game_end:
            return True
        if len(self.players) == 1:
            return True
        for player in self.players:
            if len(player.rack) == 0:
                return True
        return False

    def make_move(self, row: int, col: int, word: str, direction: Direction, current_player: Player = None):
        current_player = current_player or self.current_player
        old_player_score = current_player.score

        move = Move(row, col, word, direction, current_player)
        move.validate_move(self.board, self.settings_manager)
        move.execute(self.board, self.settings_manager)

        current_player.rack.refill(self.bag, self.settings_manager)
        if current_player.score == old_player_score:
            self.zero_score_streak += 1
        else:
            self.zero_score_streak = 0
        self.current_player = self.players[(self.players.index(current_player) + 1) % len(self.players)]
        self.is_over = self.has_ended()

    def exchange_tiles(self, tiles: str, current_player: Player = None):
        current_player = current_player or self.current_player
        current_player.exchange_tiles(tiles, self.bag, self.settings_manager)
        self.zero_score_streak += 1
        self.current_player = self.players[(self.players.index(current_player) + 1) % len(self.players)]
        self.is_over = self.has_ended()

       
    def pass_turn(self, current_player: Player = None):
        current_player = current_player or self.current_player
        self.zero_score_streak += 1
        self.current_player = self.players[(self.players.index(current_player) + 1) % len(self.players)]
        self.is_over = self.has_ended()

    def resign(self, current_player: Player = None):
        current_player = current_player or self.current_player
        self.players.remove(current_player)
        self.current_player = self.players[(self.players.index(current_player) + 1) % len(self.players)]
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
        output += self.board
        output += f'Tiles remaining: {len(self.bag)}'
        return output
    
def main():
    game = Game('scrabble_settings.json', ['Mac', 'Gyver'])
    while not game.is_over:
        print(game)
        print('Enter 1 to make a move')
        print('Enter 2 to exchange tiles')
        print('Enter 3 to pass turn')
        print('Enter 4 to resign')
        choice = input('Enter choice: ')
        if choice == '1':
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            word = input('Enter word: ')
            direction = Direction(input('Enter direction (h or v): '))
            game.make_move(row, col, word, direction)
        elif choice == '2':
            tiles = input('Enter tiles to exchange: ')
            game.exchange_tiles(tiles)
        elif choice == '3':
            game.pass_turn()
        elif choice == '4':
            game.resign()
        else:
            print('Invalid choice.')
    game.end_game()

if __name__ == '__main__':
    main()