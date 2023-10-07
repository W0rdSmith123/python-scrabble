from bag import ScrabbleBag
from rack import Rack
from settings_manager import SettingsManager
class Player:
    def __init__(self, name: str, bag: ScrabbleBag, settings_manager: SettingsManager):
        self._name = name
        self._rack = Rack(bag, settings_manager)
        self._score = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Score must be an integer!")    
        self._score = value

    @property
    def rack(self) -> Rack:
        return self._rack
    
    @rack.setter
    def rack(self, rack: Rack) -> None:
        self._rack = rack

    def refill(self, bag: ScrabbleBag) -> None:
        self.rack.refill(bag)
    
    def exchange_tiles(self, tiles: str, bag: ScrabbleBag) -> None:
        self.rack.exchange_tiles(tiles, bag)
        
    def __lt__(self: 'Player', other: 'Player') -> bool:
        return self.rack < other.rack

    def __repr__(self):
        return f'Player({self.name}, {self.score})'
    
    def __str__(self):
        return f'{self.name} ({self.score}) - Rack: {self.rack}'

