import random


class Solution:
    def modifyString(self, original_string: str) -> str:
        # https://www.educative.io/edpresso/what-are-ord-and-chr-functions-in-python
        letters = [''] * 26
        for i in range(len(letters)):
            letters[i] = chr(ord('a') + i)
        # import string
        # letters = string.ascii_lowercase
        characters = list(original_string)
        for i in range(len(characters)):
            if characters[i] == '?':
                left_character, right_character = '', ''
                letter = random.choice(letters)
                if i - 1 >= 0:
                    left_character = characters[i - 1]
                if i + 1 < len(characters):
                    right_character = characters[i + 1]
                while letter == left_character or letter == right_character:
                    letter = random.choice(letters)
                characters[i] = letter
        return ''.join(characters)
