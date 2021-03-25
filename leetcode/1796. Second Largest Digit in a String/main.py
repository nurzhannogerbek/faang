class Solution:
    def secondHighest(self, original_string: str) -> int:
        digits = [character for character in original_string if character.isdigit()]
        digits = sorted(set(digits))
        return digits[-2] if len(digits) > 1 else -1
