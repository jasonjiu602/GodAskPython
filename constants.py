from enum import Enum


class TypingGameDifficulty(Enum):
    EASY = 2
    MEDIUM = 3
    HARD = 4


class TypingGameTimeWindow(Enum):
    EASY = 5
    MEDIUM = 4
    HARD = 3


typing_game_word_map = {
    0: ["dāo", "刀", "dao"],
    1: ["qiāng", "枪", "qiang"],
    2: ["jiàn", "剑", "jian"],
    3: ["jǐ", "戟", "ji"],
    4: ["fǔ", "斧", "fu"],
    5: ["yùe", "钺", "yue"],
    6: ["gōu", "钩", "gou"],
    7: ["chā", "叉", "cha"]
}


class TypingGameMapConst:
    HINT = 0
    CHARACTER = 1
    ANSWER = 2
