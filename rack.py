from bag import ScrabbleBag
from settings_manager import SettingsManager
from tile import ScrabbleTile

class Rack:
    def __init__(self, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        self.tiles = []
        self.refill(bag, settings_manager)
        self.sort()
    
    def refill(self, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        for _ in range(min(settings_manager.max_rack_size - len(self.tiles), len(bag))):
            self.tiles.append(bag.draw_tile())
        self.sort()
    
    def exchange_tiles(self, tiles: str, bag: ScrabbleBag, settings_manager: SettingsManager) -> None:
        if len(tiles) > settings_manager.max_rack_size:
            raise ValueError('Cannot exchange more tiles than the maximum rack size')
        for tile in tiles:
            if tile not in self.tiles:
                raise ValueError('Cannot exchange tiles that are not in the rack')
        for tile in tiles:
            storedTile = self.get_tile(tile)
            self.tiles.remove(storedTile)
            bag.deposit_tile(storedTile)
        self.refill(bag, settings_manager)
    def sort(self) -> None:
        self.tiles.sort()

    def pop(self, index: int) -> ScrabbleTile:
        return self.tiles.pop(index)

    def get_tile(self, char: str) -> ScrabbleTile:
        for tile in self.tiles:
            if tile == char:
                return tile
        for tile in self.tiles:
            if tile == '#':
                tile.letter = char
                return tile
        return None

    def remove_tile(self, tile: ScrabbleTile) -> None:
        try:
            self.tiles.remove(tile)
        except ValueError:
            raise ValueError('Tile not in rack')
        

    def __lt__(self, other: 'Rack') -> bool:
        if not isinstance(other, Rack):
            raise TypeError(f'Cannot compare Player to {type(other)}')
        self.sort()
        other.sort()
        
        for i in range(min(len(self), len(other))):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        return len(self) < len(other)

    def __len__(self) -> int:
        return len(self.tiles)
    
    def __getitem__(self, index: int) -> ScrabbleTile:
        return self.tiles[index]

    def __repr__(self):
        return f'Rack({self.tiles})'
    
    def __str__(self):
        formatted_tiles = []
        for tile in self.tiles:
            formatted_tiles.append(str(tile))
        return formatted_tiles.join(' ')