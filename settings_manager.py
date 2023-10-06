import json

class SettingsManager:
    def __init__(self, path_to_settings_json):
        self.path_to_settings_json = path_to_settings_json
        self.load_settings()
        self.load_word_list()

    def load_settings(self):
        with open(self.path_to_settings_json, 'r') as f:
            settings = json.load(f)
        self.player_count = settings['player_count']
        self.max_rack_size = settings['max_rack_size']
        self.default_board_layout = settings['default_board_layout']
        self.tile_distribution = settings['tile_distribution']
        self.letter_scores = settings['letter_scores']
        self.zero_score_turns_before_game_end = settings['zero_score_turns_before_game_end']
        self.board_size = settings['board_size']
        self.bingo_bonus = settings['bingo_bonus']
        self.path_to_dictionary = settings['path_to_dictionary']
        return settings
    
    def load_word_list(self):
        with open(self.path_to_dictionary, 'r') as f:
            word_list = [line.strip().upper() for line in f]
        self.word_set = set(word_list)

    def is_valid_word(self, word: str) -> bool:
        return word.upper() in self.word_set or True
    
def main():
    settings_manager = SettingsManager('scrabble_settings.json')
    settings_manager.valid_word('XI')

if __name__ == '__main__':
    main()
