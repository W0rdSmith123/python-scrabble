from exceptions import InvalidLetterError, InvalidValueError, TileModificationError
class ScrabbleTile:
    def __init__(self, letter: str, value: int):
        if not isinstance(letter, str) or len(letter) != 1:
            raise InvalidLetterError('Letter must be a single character string')
        if not isinstance(value, int):
            raise InvalidValueError('Value must be an integer')
        if value < 0:
            raise InvalidValueError('Value must be a positive integer')
        
        self._letter = letter
        self._value = value
        self.placed_this_turn = False

    @property
    def letter(self) -> str:
        return self._letter
    
    @letter.setter
    def letter(self, new_letter: str):
        if self._letter != '#':
            raise TileModificationError("Only blank tiles can be modified!")
        if not isinstance(new_letter, str) or len(new_letter) != 1:
            raise InvalidLetterError('Letter must be a single character string')
        self._letter = new_letter

    @property
    def value(self) -> int:
        return self._value

    def place_on_board(self):
        """Method to indicate that the tile has been placed on the board this turn."""
        self.placed_this_turn = True
    
    def reset_placement_status(self):
        """Method to reset the placed_this_turn attribute after processing the move."""
        self.placed_this_turn = False

    def __repr__(self) -> str:
        return f'ScrabbleTile({self.letter}, {self.value})'
    
    def __str__(self) -> str:
        return str(self.letter) + str(self.value)
    
    def __lt__(self, other: 'ScrabbleTile') -> bool:
        return self.letter < other.letter
    
    def __gt__(self, other: 'ScrabbleTile') -> bool:
        return self.letter > other.letter
    
    def __eq__(self, other: 'ScrabbleTile') -> bool:
        if not isinstance(other, ScrabbleTile) and not isinstance(other, str):
            return False
        if isinstance(other, str):
            return self.letter.upper() == other.upper()
        return self.letter == other.letter and self.value == other.value