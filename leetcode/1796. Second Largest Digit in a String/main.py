class Solution:
    def secondHighest(self, original_string: str) -> int:
        digits = {int(character) for character in original_string if character.isdigit()}
        return sorted(digits)[-2] if len(digits) > 1 else -1
