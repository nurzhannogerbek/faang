class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = str()
        word1 = list(word1)
        word2 = list(word2)
        for i in range(min(len(word1), len(word2))):
            merged_string += word1.pop(0) + word2.pop(0)
        merged_string += ''.join(word1) + ''.join(word2)
        return merged_string
