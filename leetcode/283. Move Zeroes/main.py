class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        The first pointer i traverses the array and the second pointer j keeps track of the position where the next non-zero element should be placed.
        As we traverse the array with pointer i, we swap the current element with the element at the j-th position and increment j only when a non-zero element is encountered.
        """
        # Index to keep track of where the next non-zero element should be placed.
        j = 0

        # Traverse the array.
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current element with the element at the j-th position.
                nums[i], nums[j] = nums[j], nums[i]
                # Increment j.
                j += 1