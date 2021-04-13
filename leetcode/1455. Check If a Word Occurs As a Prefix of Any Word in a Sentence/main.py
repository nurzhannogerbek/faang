class Solution:
    def isPrefixOfWord(self, sentence: str, search_word: str) -> int:
        words = sentence.split()
        for index, word in enumerate(words):
            if word.startswith(search_word):
                return index + 1
        return -1
