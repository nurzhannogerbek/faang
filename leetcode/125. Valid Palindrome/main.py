import re


class Solution:
    def isPalindrome(self, original_string: str) -> bool:
        original_string = re.sub('[^A-Za-z0-9]+', '', original_string).lower()
        reversed_string = reversed(original_string)
        return True if list(original_string) == list(reversed_string) else False
