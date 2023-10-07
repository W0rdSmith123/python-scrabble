# Main Scrabble exception
class ScrabbleError(Exception):
    """Base exception for all Scrabble-related errors."""
    pass

# Bag exceptions
class EmptyBagError(ScrabbleError):
    """Raised when attempting to draw from an empty Scrabble bag."""
    pass

# Board exceptions
class InvalidBoardPositionError(ScrabbleError):
    """Raised when an invalid row or column is accessed on the board."""
    pass

# Game exceptions
class PlayerCountMismatchError(ScrabbleError):
    """Raised when the number of player names doesn't match the expected count."""
    pass

class TileDistributionError(ScrabbleError):
    """Raised when there are not enough tiles for the given number of players."""
    pass

# Move exceptions
class InvalidWordError(ScrabbleError):
    """Raised when an invalid word is played."""
    pass

class InvalidPlacementError(ScrabbleError):
    """Raised when tiles are placed in an invalid position."""
    pass

class TilesNotConnectedError(ScrabbleError):
    """Raised when played tiles are not connected to existing tiles."""
    pass

class InsufficientTilesError(ScrabbleError):
    """Raised when the player doesn't have the necessary tiles to make a move."""
    pass

# Rack exceptions
class RackSizeError(ScrabbleError):
    """Raised when a modification to the rack would exceed the rack size bounds."""
    pass

class TileNotInRackError(ScrabbleError):
    """Raised when a tile is not found in the rack."""
    pass

# Settings Manager exceptions
class InvalidSettingTypeError(ScrabbleError):
    """Raised when an invalid setting type is defined."""
    pass

# Square exceptions
class SquareOccupiedError(ScrabbleError):
    """Raised when trying to place a tile on an already occupied square."""
    pass

class NoTileError(ScrabbleError):
    """Raised when trying to access or remove a tile from an empty square."""
    pass

class InvalidSquareTypeError(ScrabbleError):
    """Raised when an invalid square type is used."""
    pass
    
# Tile exceptions
class InvalidLetterError(ScrabbleError):
    """Raised for invalid letter assignments."""
    pass

class InvalidValueError(ScrabbleError):
    """Raised for invalid value assignments."""
    pass

class NonBlankTileError(ScrabbleError):
    """Raised when trying to modify a non-blank tile."""
    pass
