class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            if left_sum == (total_sum - left_sum - value):
                return index
            left_sum += value
        return -1