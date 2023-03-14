class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        # Move along the input array starting from the end.
        for i in range(length):
            idx = length - 1 - i
            # Set all the nines at the end of array to zeros.
            if digits[idx] == 9:
                digits[idx] = 0
            # Here we have the rightmost not-nine.
            else:
                # increase this rightmost not-nine by 1.
                digits[idx] += 1
                return digits
        # We're here because all the digits are nines.
        return [1] + digits
