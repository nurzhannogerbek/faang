class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Approach 1: Sliding Window
        longest_sequence, left, right, num_zeroes = 0, 0, 0, 0
        # While our window is in bounds.
        while right < len(nums):
            # Add the right most element into our window.
            if nums[right] == 0:
                num_zeroes += 1
            # If our window is invalid, contract our window.
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            # Update our longest sequence answer.
            longest_sequence = max(longest_sequence, right - left + 1)
            # Expand our window.
            right += 1
        return longest_sequence

        # Approach 2
        # Initialize variables to keep track of the longest sequence and the current sequence.
        # max_sequence = 0
        # current_sequence = 0
        # Initialize a variable to keep track of the index of the last zero.
        # last_zero = -1

        # Iterate over the array.
        # for i in range(len(nums)):
            # If the current element is a 1, increase the current sequence length.
            # if nums[i] == 1:
                # current_sequence += 1
            # If the current element is a 0, calculate the length of the sequence with one change.
            # else:
                # If this is the first zero, just add it to the current sequence.
                # if last_zero == -1:
                    # current_sequence += 1
                # Otherwise, calculate the length of the sequence with one change.
                # else:
                    # Update the max sequence if the current sequence plus the length of the sequence from the last zero to the current position is greater than the current max sequence.
                    # max_sequence = max(max_sequence, current_sequence)
                    # Reset the current sequence to be the length of the sequence from the last zero to the current position.
                    # current_sequence = i - last_zero
                # Update the index of the last zero.
                # last_zero = i

        # If the last element was a 1, check if the current sequence length plus the length of the sequence from the last zero to the end of the array is greater than the current max sequence.
        # if nums[-1] == 1:
            # max_sequence = max(max_sequence, current_sequence)
        # Otherwise, check if the current sequence length plus the length of the sequence from the last zero to the end of the array is greater than the current max sequence.
        # else:
            # max_sequence = max(max_sequence, current_sequence + 1)

        # Return the max sequence.
        # return max_sequence
