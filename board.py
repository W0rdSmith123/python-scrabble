from square import ScrabbleSquare
from enums import SquareType, Direction
class ScrabbleBoard:
    def __init__(self, default_board_layout: list[list[str]]):
        self.board = []
        for row in default_board_layout:
            self.board.append([ScrabbleSquare(SquareType(square)) for square in row])

    def get_square(self, row: int, col: int) -> ScrabbleSquare:
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            raise IndexError('Row or column out of bounds')
        return self.board[row][col]
    
    def validate_move(self, row: int, col: int, word: str, direction: Direction) -> None:
        offset = len(word) - 1
        self.get_square(row, col)  # Check if the starting square is valid
        self.get_square(row + (direction == Direction.VERTICAL) * offset, col + (direction == Direction.HORIZONTAL) * offset)

    def __repr__(self):
        return f'ScrabbleBoard({len(self.board)})'

    def __str__(self):
        output = '   ' + ' '.join([f'{i:2}' for i in range(len(self.board[0]))]) + '\n'  # Column headers
        output += '   ' + '+--' * len(self.board[0]) + '+\n'  # Top border
        for i, row in enumerate(self.board):
            output += f'{i:2} |'  # Row header
            for square in row:
                string = str(square)
                if len(string) == 1:
                    string = string + ' '
                output += f'{string}|'
            output += '\n'
            output += '   ' + '+--' * len(self.board[0]) + '+\n'  # Bottom border for each row
        return output

    def __getitem__(self, index: int) -> list[ScrabbleSquare]:
        return self.board[index]