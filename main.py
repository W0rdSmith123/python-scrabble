import json

from enums import Direction
from game import Game
from exceptions import InvalidWordError

def main():
    with open('enable.txt') as f:
        word_set = set(f.read().splitlines())
    with open('scrabble_settings.json') as f:
        settings_dict = json.load(f)
    game = Game(word_set, settings_dict, ['Mac', 'Gyver'])
    while not game.is_over:
        print(game)
        print('Enter 1 to make a move')
        print('Enter 2 to exchange tiles')
        print('Enter 3 to pass turn')
        print('Enter 4 to resign')
        choice = input('Enter choice: ')
        if choice == '1':
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            word = input('Enter word: ')
            direction = Direction(input('Enter direction (h or v): '))
            try:
                game.make_move(row, col, word, direction)
            except InvalidWordError as e:
                print(e)

        elif choice == '2':
            tiles = input('Enter tiles to exchange: ')
            game.exchange_tiles(tiles)
        elif choice == '3':
            game.pass_turn()
        elif choice == '4':
            game.resign()
        else:
            print('Invalid choice.')
    game.apply_end_game_penalties()
    players = sorted(game.players, key=lambda player: player.score, reverse=True)
    for player in players:
        print(f'{player.name}\'s score: {player.score}')


if __name__ == '__main__':
    main()