class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Approach 1: Sort.
        # nums.sort(key=lambda x: x%2)
        # return nums

        # Approach 2: In-Place.
        # If we want to do the sort in-place, we can use quicksort algorithm.
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1
        return nums