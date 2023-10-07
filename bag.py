import random

from exceptions import EmptyBagError
from settings_manager import SettingsManager
from tile import ScrabbleTile

class ScrabbleBag:
    """
    Represents a bag of Scrabble tiles.
    Allows drawing and depositing tiles, shuffling the tiles, and checking the count.
    """

    def __init__(self, settings_manager: SettingsManager):
        letter_scores = settings_manager.tile_scoring.letter_scores
        tiles = settings_manager.tile_scoring.tile_distribution

        self._tiles = [ScrabbleTile(letter, letter_scores[letter]) for letter, quantity in tiles.items() for _ in range(quantity)]
        self._tiles = self._tiles
        random.shuffle(self._tiles)
        self._tiles = self._tiles[:20]

    def draw_tile(self) -> ScrabbleTile:
        """Draw a random tile from the bag. Raises an error if the bag is empty."""
        if not self._tiles:
            raise EmptyBagError('Bag is empty')
        return self._tiles.pop(random.randint(0, len(self._tiles) - 1))

    def deposit_tile(self, tile: ScrabbleTile) -> None:
        """Deposit a tile back into the bag and shuffle."""
        self._tiles.append(tile)

    @property
    def tiles(self) -> list[ScrabbleTile]:
        """Get a copy of the list of tiles without allowing modification to the original list."""
        return self._tiles.copy()

    def __len__(self) -> int:
        """Return the number of tiles in the bag."""
        return len(self._tiles)