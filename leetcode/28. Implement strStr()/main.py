class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            index = 0
        else:
            try:
                index = haystack.index(needle)
            except ValueError:
                index = -1
        return index
