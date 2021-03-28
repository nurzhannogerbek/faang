class Solution:
    def lengthOfLastWord(self, original_string: str) -> int:
        return len(original_string.split()[-1]) if len(original_string.split()) > 0 else 0
