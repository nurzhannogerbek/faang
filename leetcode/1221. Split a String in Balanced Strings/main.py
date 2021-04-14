class Solution:
    def balancedStringSplit(self, original_string: str) -> int:
        balance = count = 0
        for character in original_string:
            if character == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
