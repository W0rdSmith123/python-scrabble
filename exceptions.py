# Base exceptions
class ScrabbleError(Exception):
    """Base exception for all Scrabble-related errors."""
    pass

class ScrabbleValueError(ScrabbleError, ValueError):
    """Base exception for value-related errors in Scrabble."""
    pass

# Bag-related exceptions
class EmptyBagError(ScrabbleError):
    """Raised when an attempt is made to draw a tile from an empty bag."""
    pass

# Board-related exceptions
class OutOfBoundsError(ScrabbleError):
    """Raised when an attempt is made to access a square outside the board boundaries."""
    pass

class InvalidMoveError(ScrabbleError):
    """Raised when a move on the board is invalid."""
    pass

class InvalidPlacementError(ScrabbleError):
    """Raised when trying to place tiles in a disconnected manner on the board."""
    pass

class TilePlacementError(ScrabbleValueError):
    """Raised when trying to place a tile on a square that's already occupied."""
    pass

class InvalidWordError(ScrabbleValueError):
    """Raised when an invalid word is used in a move."""
    pass

class InvalidNormalWordError(ScrabbleValueError):
    """Raised when the tiles placed form an invalid perpendicular word."""
    pass

# Player-related exceptions
class InvalidPlayerAction(ScrabbleError):
    """Raised when the player attempts an invalid action."""
    pass

# Input-related exceptions
class InvalidInputError(ScrabbleError):
    """Raised when the input provided is invalid."""
    pass

# Rack-related exceptions
class RackError(ScrabbleError):
    """Base exception for rack-related errors."""
    pass

class InvalidTileExchange(RackError):
    """Raised when trying to exchange invalid tiles."""
    pass

class TileNotFound(RackError):
    """Raised when a specific tile is not found in the rack."""
    pass

# Tile-related exceptions
class InvalidLetterError(ScrabbleValueError):
    """Raised when the letter provided is invalid."""
    pass

class NoTileError(ScrabbleValueError):
    """Raised when an operation requires a tile but the square is empty."""
    pass

class TileModificationError(ScrabbleValueError):
    """Raised when attempting to modify an immutable tile."""
    pass

# Setting-related exceptions
class InvalidSettingError(ScrabbleValueError):
    """Raised when a setting has an invalid type or value."""
    pass

class InvalidValueError(ScrabbleValueError):
    """Raised when the value provided is invalid."""
    pass
