class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        # https://www.youtube.com/watch?v=wyH7i8HmoPM
        dictionary = {}
        for letter in set(ransom_note):
            dictionary[letter] = ransom_note.count(letter)
        for letter in dictionary:
            if letter not in magazine:
                return False
            elif magazine.count(letter) < dictionary[letter]:
                return False
        return True
