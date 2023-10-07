# Main Scrabble exception
class ScrabbleException(Exception):
    """Base exception for all Scrabble-related errors."""
    pass

# Bag exceptions
class EmptyBagError(ScrabbleException):
    """Raised when attempting to draw from an empty Scrabble bag."""
    pass

# Board exceptions
class InvalidBoardPositionError(ScrabbleException):
    """Raised when an invalid row or column is accessed on the board."""
    pass

# Game exceptions
class PlayerCountMismatchError(ScrabbleException):
    """Raised when the number of player names doesn't match the expected count."""
    pass

class TileDistributionError(ScrabbleException):
    """Raised when there are not enough tiles for the given number of players."""
    pass

# Move exceptions
class InvalidWordError(ScrabbleException):
    """Raised when an invalid word is played."""
    pass

class InvalidPlacementError(ScrabbleException):
    """Raised when tiles are placed in an invalid position."""
    pass

class TilesNotConnectedError(ScrabbleException):
    """Raised when played tiles are not connected to existing tiles."""
    pass

class InsufficientTilesError(ScrabbleException):
    """Raised when the player doesn't have the necessary tiles to make a move."""
    pass

# Rack exceptions
class RackSizeError(ScrabbleException):
    """Raised when a modification to the rack would exceed the rack size bounds."""
    pass

class TileNotInRackError(ScrabbleException):
    """Raised when a tile is not found in the rack."""
    pass

# Settings Manager exceptions
class InvalidSettingTypeError(ScrabbleException):
    """Raised when an invalid setting type is defined."""
    pass

# Square exceptions
class SquareOccupiedError(ScrabbleException):
    """Raised when trying to place a tile on an already occupied square."""
    pass

class NoTileError(ScrabbleException):
    """Raised when trying to access or remove a tile from an empty square."""
    pass

class InvalidSquareTypeError(ScrabbleException):
    """Raised when an invalid square type is used."""
    pass
    
# Tile exceptions
class InvalidLetterError(ScrabbleException):
    """Raised for invalid letter assignments."""
    pass

class InvalidValueError(ScrabbleException):
    """Raised for invalid value assignments."""
    pass

class NonBlankTileError(ScrabbleException):
    """Raised when trying to modify a non-blank tile."""
    pass
