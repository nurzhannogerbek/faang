class Solution:
    def secondHighest(self, original_string: str) -> int:
        basket = set()
        for character in original_string:
            if character.isdigit():
                basket.add(int(character))
        if len(basket) > 1:
            return sorted(basket)[-2]
        else:
            return -1
