from bag import ScrabbleBag
from exceptions import InvalidTileExchange, TileNotFound
from settings_manager import SettingsManager
from tile import ScrabbleTile

class Rack:
    def __init__(self, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        self._tiles: list[ScrabbleTile] = []
        self._max_rack_size = settings_manager.game_mechanics.max_rack_size
        self.refill(bag)

    @property
    def tiles(self) -> list[ScrabbleTile]:
        return self._tiles

    @property
    def max_rack_size(self) -> int:
        return self._max_rack_size

    def refill(self, bag: ScrabbleBag) -> None:
        for _ in range(min(len(bag), self.max_rack_size - len(self))):
            self._tiles.append(bag.draw_tile())
        self.sort()

    def exchange_tiles(self, tiles: str, bag: ScrabbleBag) -> None:
        if len(tiles) > self.max_rack_size:
            raise InvalidTileExchange('Cannot exchange more tiles than the maximum rack size')
        for tile in tiles:
            if not self.has_tile(tile):
                raise InvalidTileExchange(f"Tile '{tile}' not found in rack")
        for tile in tiles:
            storedTile = self.get_tile(tile)
            self._tiles.remove(storedTile)
            bag.deposit_tile(storedTile)
        self.refill(bag)

    def has_tile(self, char: str) -> bool:
        return any(tile == char or (tile == '#' and char != '#') for tile in self._tiles)

    def sort(self) -> None:
        self._tiles.sort()

    def pop(self, index: int) -> ScrabbleTile:
        return self._tiles.pop(index)

    def get_tile(self, char: str) -> ScrabbleTile:
        for tile in self._tiles:
            if tile == char:
                return tile
        for tile in self._tiles:
            if tile == '#':
                tile.letter = char
                return tile
        raise TileNotFound(f"Tile '{char}' not found in rack")

    def remove_tile(self, tile: ScrabbleTile) -> None:
        try:
            self._tiles.remove(tile)
        except ValueError:
            raise TileNotFound('Tile not in rack')

    def __lt__(self, other: 'Rack') -> bool:
        if not isinstance(other, Rack):
            raise TypeError(f'Cannot compare Rack to {type(other)}')
        for i in range(min(len(self), len(other))):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        return len(self) < len(other)

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: int) -> ScrabbleTile:
        return self._tiles[index]

    def __repr__(self):
        return f'Rack({self._tiles})'

    def __str__(self):
        return ' '.join(str(tile) for tile in self._tiles)