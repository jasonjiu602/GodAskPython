from random import randint
import time
import threading
from constants import TypingGameDifficulty, TypingGameTimeWindow, typing_game_word_map, TypingGameMapConst


class TypingGame:

    def __init__(self, difficulty=TypingGameDifficulty.MEDIUM, time_window = TypingGameTimeWindow.MEDIUM, is_sort=True):
        self.difficulty = difficulty
        self.time_window = time_window
        self.is_sort = is_sort

    def timing_func(self):
        count = self.time_window.value
        while count > 0:
            count -= 1
            print(f"{count} seconds left!")
            time.sleep(1)

    def generate_words(self):
        word = ""
        word_hint = ""
        answer = ""

        for character_num in range(0, self.difficulty.value):
            curr_num = randint(0, len(typing_game_word_map) - 1)
            print(curr_num)
            word += typing_game_word_map[curr_num][TypingGameMapConst.CHARACTER] + " "
            word_hint += typing_game_word_map[curr_num][TypingGameMapConst.HINT] + " "
            answer += typing_game_word_map[curr_num][TypingGameMapConst.ANSWER]
        return [word, word_hint, answer]

    @staticmethod
    def typing_stage(word, word_hint, word_answer):
        input_hint = f"请输入！\n{word_hint}\n{word}:\n"
        user_input = input(input_hint)
        if user_input != word_answer:
            return False
        else:
            return True

    def checking_typing(self):
        word, word_hint, word_answer = self.generate_words()
        flag = self.typing_stage(word, word_hint, word_answer)
        print(flag)



if __name__ == '__main__':
    typing_game = TypingGame()
    temp_var = typing_game.checking_typing()