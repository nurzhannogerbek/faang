class Solution:
    def reverseVowels(self, original_string: str) -> str:
        vowels = set('aeiouAEIOU')
        word_vowels = [char for char in original_string if char in vowels]
        result = str()
        for char in original_string:
            if char in vowels:
                result += word_vowels.pop()
            else:
                result += char
        return result
