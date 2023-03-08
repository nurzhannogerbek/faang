class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two indexes approach.
        # First Index is responsible for writing unique values in our input array, while Second Index will read the input array and pass all the distinct elements to First Index.
        size = len(nums)
        insert_index = 1
        for i in range(1, size):
            # Found unique element.
            if nums[i - 1] != nums[i]:
                # Updating insert_index in our main array.
                nums[insert_index] = nums[i]
                # Incrementing insert_index count by 1.
                insert_index += 1
        return insert_index
