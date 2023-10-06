class ScrabbleTile:
    def __init__(self, letter: str, value: int):
        if not isinstance(letter, str) or len(letter) != 1:
            raise TypeError('Letter must be a single character string')
        if not isinstance(value, int):
            raise TypeError('Value must be an integer')
        if value < 0:
            raise ValueError('Value must be a positive integer')
        self.letter = letter
        self.value = value
        self.placed_this_turn = None

    def __repr__(self):
        return f'ScrabbleTile({self.letter}, {self.value})'
    
    def __str__(self):
        return str(self.letter) + str(self.value)
    
    def __lt__(self, other):
        return self.letter < other.letter
    
    def __gt__(self, other):
        return self.letter > other.letter
    
    def __eq__(self, other):
        if not isinstance(other, ScrabbleTile) and not isinstance(other, str):
            return False
        if isinstance(other, str):
            return self.letter.upper() == other.upper()
        return self.letter == other.letter and self.value == other.value