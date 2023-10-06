import random

from tile import ScrabbleTile

class ScrabbleBag:
    def __init__(self, tiles: dict[str, int], letter_scores: dict[str, int]):
        self.tiles = []
        for letter, quantity in tiles.items():
            for _ in range(quantity):
                self.tiles.append(ScrabbleTile(letter, letter_scores[letter]))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.tiles)
    
    def draw_tile(self):
        if len(self.tiles) == 0:
            raise IndexError('Bag is empty')
        return self.tiles.pop()
    
    def deposit_tile(self, tile: ScrabbleTile):
        self.tiles.append(tile)
        self.shuffle()
    
    def __len__(self):
        return len(self.tiles)