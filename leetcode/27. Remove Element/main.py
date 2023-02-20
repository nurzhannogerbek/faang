class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two Pointers Approach.
        reader, writer = 0, 0
        n = len(nums)
        while reader < n :
            if nums[reader] == val:
                reader += 1
            else:
                nums[writer] = nums[reader]
                reader += 1
                writer += 1
        return writer
