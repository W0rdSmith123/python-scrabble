from typing import Any, Dict, List, Optional, Set

from exceptions import InvalidSettingTypeError

DEFAULT_SETTINGS = {
    "player_count": 2,
    "bingo_bonus": 50,
    "max_rack_size": 7,
    "zero_score_turns_before_game_end": 6,
    "board_size": 15,
    "default_board_layout":
      [
          ["TW", "  ", "  ", "DL", "  ", "  ", "  ", "TW", "  ", "  ", "  ", "DL", "  ", "  ", "TW"],
          ["  ", "DW", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "DW", "  "],
          ["  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  "],
          ["DL", "  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  ", "DL"],
          ["  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  "],
          ["  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  "],
          ["  ", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "  "],
          ["TW", "  ", "  ", "DL", "  ", "  ", "  ", "ST", "  ", "  ", "  ", "DL", "  ", "  ", "TW"],
          ["  ", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DL", "  ", "  "],
          ["  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  "],
          ["  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  ", "  ", "DW", "  ", "  ", "  ", "  "],
          ["DL", "  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  ", "DL"],
          ["  ", "  ", "DW", "  ", "  ", "  ", "DL", "  ", "DL", "  ", "  ", "  ", "DW", "  ", "  "],
          ["  ", "DW", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "TL", "  ", "  ", "  ", "DW", "  "],
          ["TW", "  ", "  ", "DL", "  ", "  ", "  ", "TW", "  ", "  ", "  ", "DL", "  ", "  ", "TW"]
      ],
    "tile_distribution": {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1,
        "#": 2
    },
    "letter_scores": {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
        "#": 0
    }    
}



class SettingsManager:
    def __init__(self, word_set: set, settings_dict: Optional[Dict[str, Any]] = None) -> None:
        self._settings = settings_dict or {}
        self.game_mechanics = self.GameMechanics(self)
        self.board_settings = self.BoardSettings(self)
        self.tile_scoring = self.TileScoring(self)
        self.load_word_set(word_set)

    def _get_setting(self, key: str) -> Any:
        """Retrieve a setting value or its default."""
        return self._settings.get(key, DEFAULT_SETTINGS[key])

    def _set_setting_with_validation(self, key: str, value: Any, *expected_types: Any) -> None:
        """Set a setting value after type validation."""
        self._validate_types(key, value, expected_types)
        self._settings[key] = value

    def _validate_types(self, key: str, value: Any, expected_types: tuple) -> None:
        """Validates types of provided value against expected types."""
        if not isinstance(value, expected_types[0]):
            raise InvalidSettingTypeError(f"{key} must be of type {expected_types[0].__name__}.")
        if len(expected_types) > 1:
            if not all(isinstance(item, expected_types[1]) for item in value):
                raise InvalidSettingTypeError(f"Each item in {key} must be of type {expected_types[1].__name__}.")        

    class GameMechanics:
        def __init__(self, parent: 'SettingsManager') -> None:
            self.parent = parent

        @property
        def player_count(self) -> int:
            return self.parent._get_setting("player_count")

        @player_count.setter
        def player_count(self, value: int) -> None:
            self.parent._set_setting_with_validation("player_count", value, int)

        @property
        def bingo_bonus(self) -> int:
            return self.parent._get_setting("bingo_bonus")

        @bingo_bonus.setter
        def bingo_bonus(self, value: int) -> None:
            self.parent._set_setting_with_validation("bingo_bonus", value, int)

        @property
        def max_rack_size(self) -> int:
            return self.parent._get_setting("max_rack_size")

        @max_rack_size.setter
        def max_rack_size(self, value: int) -> None:
            self.parent._set_setting_with_validation("max_rack_size", value, int)

        @property
        def zero_score_turns_before_game_end(self) -> int:
            return self.parent._get_setting("zero_score_turns_before_game_end")

        @zero_score_turns_before_game_end.setter
        def zero_score_turns_before_game_end(self, value: int) -> None:
            self.parent._set_setting_with_validation("zero_score_turns_before_game_end", value, int)

    class BoardSettings:
        def __init__(self, parent: 'SettingsManager') -> None:
            self.parent = parent

        @property
        def board_size(self) -> int:
            return self.parent._get_setting("board_size")

        @board_size.setter
        def board_size(self, value: int) -> None:
            self.parent._set_setting_with_validation("board_size", value, int)

        @property
        def default_board_layout(self) -> List[List[str]]:
            return self.parent._get_setting("default_board_layout")

        @default_board_layout.setter
        def default_board_layout(self, value: List[List[str]]) -> None:
            self.parent._set_setting_with_validation("default_board_layout", value, list, list, str)

    class TileScoring:
        def __init__(self, parent: 'SettingsManager') -> None:
            self.parent = parent

        @property
        def tile_distribution(self) -> Dict[str, int]:
            return self.parent._get_setting("tile_distribution")

        @tile_distribution.setter
        def tile_distribution(self, value: Dict[str, int]) -> None:
            self.parent._set_setting_with_validation("tile_distribution", value, dict)

        @property
        def letter_scores(self) -> Dict[str, int]:
            return self.parent._get_setting("letter_scores")

        @letter_scores.setter
        def letter_scores(self, value: Dict[str, int]) -> None:
            self.parent._set_setting_with_validation("letter_scores", value, dict)

    @property
    def word_set(self) -> Set[str]:
        """Returns the word set for the game."""
        temp = self._settings.get("word_set")
        if not temp:
            raise ValueError("Word set not loaded.")
        return temp

    @word_set.setter
    def word_set(self, value: Set[str]) -> None:
        self._set_setting_with_validation("word_set", value, set)

    def load_word_set(self, word_set: set) -> None:
        """Loads the word set into the game settings."""
        self.word_set = word_set

    def is_valid_word(self, word: str) -> bool:
        """Checks if a word is valid."""
        return word.lower() in self.word_set