from typing import Union

from exceptions import InvalidLetterError, InvalidValueError, NonBlankTileError

class ScrabbleTile:
    def __init__(self, letter: str, value: int):
        if not isinstance(letter, str) or len(letter) != 1:
            raise InvalidLetterError()
        if not isinstance(value, int) or value < 0:
            raise InvalidValueError()

        self._letter = letter
        self._value = value
        self.placed_this_turn = False

    @property
    def letter(self) -> str:
        return self._letter

    @letter.setter
    def letter(self, new_letter: str):
        if self._letter != '#':
            raise NonBlankTileError()
        if not isinstance(new_letter, str) or len(new_letter) != 1:
            raise InvalidLetterError()
        self._letter = new_letter

    @property
    def value(self) -> int:
        return self._value

    def place_on_board(self) -> None:
        """Method to indicate that the tile has been placed on the board this turn."""
        self.placed_this_turn = True
    
    def reset_placement_status(self) -> None:
        """Method to reset the placed_this_turn attribute after processing the move."""
        self.placed_this_turn = False

    def __repr__(self) -> str:
        return f'ScrabbleTile({self.letter}, {self.value})'
    
    def __str__(self) -> str:
        return str(self.letter) + str(self.value)
    
    def __lt__(self, other: 'ScrabbleTile') -> bool:
        """Tiles are sorted based on their letters."""
        return self.letter < other.letter
    
    def __gt__(self, other: 'ScrabbleTile') -> bool:
        """Tiles are sorted based on their letters."""
        return self.letter > other.letter
    
    def __eq__(self, other: Union['ScrabbleTile', str]) -> bool:
        """Tiles are equal if their letters (case insensitive) and values match. Also allows comparison with a string."""
        if isinstance(other, str):
            return self.letter.upper() == other.upper()
        if not isinstance(other, ScrabbleTile):
            return False
        return self.letter == other.letter and self.value == other.value