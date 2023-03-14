class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        if sorted_nums[-1] >= (2 * sorted_nums[-2]):
            return nums.index(sorted_nums[-1])
        else:
            return -1