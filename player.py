from bag import ScrabbleBag
from rack import Rack
from settings_manager import SettingsManager
from enums import PlayerType
class Player:
    def __init__(self, name: str, bag: ScrabbleBag, settings_manager: SettingsManager, player_type: PlayerType = PlayerType.HUMAN):
        self.name = name
        self.rack = Rack(bag, settings_manager)
        self.score = 0
        self.player_type = player_type
    
    def refill(self, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        self.rack.refill(bag, settings_manager)
    
    def exchange_tiles(self, tiles: str, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        self.rack.exchange_tiles(tiles, bag, settings_manager)
        

    def __lt__(self: 'Player', other: 'Player') -> bool:
        return self.rack < other.rack


    def __repr__(self):
        return f'Player({self.name}, {self.score})'
    
    def __str__(self):
        return f'{self.name} ({self.score})'