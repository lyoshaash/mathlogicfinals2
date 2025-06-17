'''
def plustwosticks(word):
    return '||' + word

word = input("введите |: ")

if all(c == '|' for c in word):
    result = plustwosticks(word)
    print("результат:", result)
    print("это число в десятичной системе:", len(result))
else:
    print("ошибка: можно вводить только символы |")
'''

from typing import List, Tuple

class Markovalgorithm:
    def __init__(self, rules: List[Tuple[str, str, bool]]):
        self.rules = rules

    def apply(self, word: str) -> str:
        while True:
            for left, right, terminal in self.rules:
                idx = word.find(left)
                if idx != -1:
                    word = word[:idx] + right + word[idx + len(left):]
                    if terminal:
                        return word
                    break
            else:
                return word

rules = [
    ("", "||", True)  # → || !
]


algo = Markovalgorithm(rules)

user_input = input("введите |: ")


if all(c == '|' for c in user_input):
    result = algo.apply(user_input)
    print("результат:", result)
    print("это число в десятичной системе", len(result))
else:
    print("ошибка: можно вводить только символы |")

