from bag import ScrabbleBag
from rack import Rack
from settings_manager import SettingsManager
from enums import PlayerType
from exceptions import InvalidPlayerAction
class Player:
    def __init__(self, name: str, bag: ScrabbleBag, settings_manager: SettingsManager, player_type: PlayerType = PlayerType.HUMAN):
        self._name = name
        self._rack = Rack(bag, settings_manager)
        self._score = 0
        self._player_type = player_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        if value < 0:
            raise InvalidPlayerAction("Score cannot be negative!")
        self._score = value

    @property
    def rack(self) -> Rack:
        return self._rack
    
    @rack.setter
    def rack(self, rack: Rack) -> None:
        self._rack = rack

    @property
    def player_type(self) -> PlayerType:
        return self._player_type

    def add_points(self, points: int) -> None:
        """Method to add points to the player's score."""
        if points < 0:
            raise InvalidPlayerAction("Cannot add negative points!")
        self._score += points

    def subtract_points(self, points: int) -> None:
        """Method to subtract points from the player's score."""
        if points < 0:
            raise InvalidPlayerAction("Cannot subtract negative points!")
        if points > self._score:
            raise InvalidPlayerAction("Cannot subtract more points than current score!")
        self._score -= points

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

