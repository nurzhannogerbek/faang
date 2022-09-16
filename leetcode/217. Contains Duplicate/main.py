"""
# The 1 method using brute force.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                return True
    return False


# The 2 method using sorting.
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return True
    return False


# The 3 method using Hash Table.
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(self, nums: List[int]) -> bool:
    storage = set()
    for value in nums:
        if value in storage:
            return True
        storage.add(value)

    return False
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
