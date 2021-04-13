class Solution:
    def reverseWords(self, original_string: str) -> str:
        return ' '.join([word[::-1] for word in original_string.split()])
