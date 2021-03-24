class Solution:
    def secondHighest(self, original_string: str) -> int:
        digits = set()
        for character in original_string:
            if character.isdigit():
                digits.add(int(character))
        if len(digits) < 2:
            return -1
        else:
            return sorted(digits)[-2]
