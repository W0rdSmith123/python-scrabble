from typing import Any, Dict, List, Optional, Set

from exceptions import InvalidSettingError

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
        self.game_mechanics = self.GameMechanics(self._settings)
        self.board_settings = self.BoardSettings(self._settings)
        self.tile_scoring = self.TileScoring(self._settings)
        self.load_word_set(word_set)

    @staticmethod
    def _get_setting(settings: dict, key: str) -> Any:
        return settings.get(key, DEFAULT_SETTINGS[key])
        
    class GameMechanics:
        def __init__(self, settings: Dict[str, Any]) -> None:
            self._settings = settings
            
        @property
        def player_count(self) -> int:
            return SettingsManager._get_setting(self._settings, "player_count")

        @player_count.setter
        def player_count(self, value: int) -> None:
            SettingsManager._validate_types(value, "player_count", int)
            self._settings["player_count"] = value

        @property
        def bingo_bonus(self) -> int:
            return SettingsManager._get_setting(self._settings, "bingo_bonus")

        @bingo_bonus.setter
        def bingo_bonus(self, value: int) -> None:
            SettingsManager._validate_types(value, "bingo_bonus", int)
            self._settings["bingo_bonus"] = value

        @property
        def max_rack_size(self) -> int:
            return SettingsManager._get_setting(self._settings, "max_rack_size")

        @max_rack_size.setter
        def max_rack_size(self, value: int) -> None:
            SettingsManager._validate_types(value, "max_rack_size", int)
            self._settings["max_rack_size"] = value

        @property
        def zero_score_turns_before_game_end(self) -> int:
            return SettingsManager._get_setting(self._settings, "zero_score_turns_before_game_end")

        @zero_score_turns_before_game_end.setter
        def zero_score_turns_before_game_end(self, value: int) -> None:
            SettingsManager._validate_types(value, "zero_score_turns_before_game_end", int)
            self._settings["zero_score_turns_before_game_end"] = value

    class BoardSettings:
        def __init__(self, settings: Dict[str, Any]) -> None:
            self._settings = settings
            
        @property
        def board_size(self) -> int:
            return SettingsManager._get_setting(self._settings, "board_size")

        @board_size.setter
        def board_size(self, value: int) -> None:
            SettingsManager._validate_types(value, "board_size", int)
            self._settings["board_size"] = value

        @property
        def default_board_layout(self) -> List[List[str]]:
            return SettingsManager._get_setting(self._settings, "default_board_layout")

        @default_board_layout.setter
        def default_board_layout(self, value: List[List[str]]) -> None:
            SettingsManager._validate_types(value, "default_board_layout", list, list, str)
            self._settings["default_board_layout"] = value

    class TileScoring:
        def __init__(self, settings: Dict[str, Any]) -> None:
            self._settings = settings

        @property
        def tile_distribution(self) -> Dict[str, int]:
            return SettingsManager._get_setting(self._settings, "tile_distribution")

        @tile_distribution.setter
        def tile_distribution(self, value: Dict[str, int]) -> None:
            SettingsManager._validate_types(value, "tile_distribution", dict, str, int)
            self._settings["tile_distribution"] = value

        @property
        def letter_scores(self) -> Dict[str, int]:
            return SettingsManager._get_setting(self._settings, "letter_scores")

        @letter_scores.setter
        def letter_scores(self, value: Dict[str, int]) -> None:
            SettingsManager._validate_types(value, "letter_scores", dict, str, int)
            self._settings["letter_scores"] = value

    @property
    def word_set(self) -> Set[str]:
        """Returns the word set for the game."""
        temp = self._settings.get("word_set")
        if not temp:
            raise InvalidSettingError("Word set not loaded.")
        return temp


    @word_set.setter
    def word_set(self, value: Set[str]) -> None:
        self._validate_types(value, "word_set", set, str)
        self._settings["word_set"] = value

    @staticmethod
    def _validate_types(value: Any, key: str, type1: Any, type2: Any = None, type3: Any = None) -> None:
        """Validates types of provided value."""
        if not isinstance(value, type1):
            raise InvalidSettingError(f"{key} must be of type {type1.__name__}.")

        if type2 and isinstance(value, (list, set, dict)):
            if not all(isinstance(item, type2) for item in value):
                raise InvalidSettingError(f"Each item in {key} must be of type {type2.__name__}.")

            if type3:
                for item in value:
                    if isinstance(item, (list, set, dict)) and not all(isinstance(inner_item, type3) for inner_item in item):
                        raise InvalidSettingError(f"Each inner item in {key} must be of type {type3.__name__}.")

    def load_word_set(self, word_set: set) -> None:
        """Loads the word set into the game settings."""
        self.word_set = word_set

    def is_valid_word(self, word: str) -> bool:
        """Checks if a word is valid."""
        return word.lower() in self.word_set