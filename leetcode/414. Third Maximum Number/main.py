class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        # Approach 2: Ordered Set.
        min_heap = []
        taken = set()

        for index in range(len(nums)):
            # If current number was already taken, skip it.
            if nums[index] in taken:
                continue

            # If min heap already has three numbers in it.
            # Pop the smallest if current number is bigger than it.
            if len(min_heap) == 3:
                if min_heap[0] < nums[index]:
                    taken.remove(min_heap[0])
                    heappop(min_heap)

                    heappush(min_heap, nums[index])
                    taken.add(nums[index])

            # If min heap does not have three number we can push it.
            else:
                heappush(min_heap, nums[index])
                taken.add(nums[index])

        # 'nums' has only one distinct element it will be the maximum.
        if len(min_heap) == 1:
            return min_heap[0]

        # 'nums' has two distinct elements.
        elif len(min_heap) == 2:
            first_num = min_heap[0]
            heappop(min_heap)
            return max(first_num, min_heap[0])

        return min_heap[0]

        # Approach 3: Ordered Set.
        # Sorted set to keep elements in sorted order.
        sorted_nums = SortedSet()

        # Iterate on all elements of 'nums' array.
        for num in nums:
            # Do not insert same element again.
            if num in sorted_nums:
                continue

            # If sorted set has 3 elements.
            if len(sorted_nums)== 3:
                # And the smallest element is smaller than current element.
                if sorted_nums[0] < num:
                    # Then remove the smallest element and push the current element.
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(num)
            # Otherwise push the current element of nums array.
            else:
                sorted_nums.add(num)

        # If sorted set has three elements return the smallest among those 3.
        if len(sorted_nums) == 3:
            return sorted_nums[0]

        # Otherwise return the biggest element of nums array.
        return sorted_nums[-1]
        """
        # Approach 1: Sorting.
        # Sort the array.
        nums.sort(reverse=True)

        #  It counts the number of distinct numbers that occurred till now.
        element_counted = 1
        # It denotes the previous counted number of the array.
        previous_element = nums[0]

        for index in range(len(nums)):
            # Current element is different from previous.
            if nums[index] != previous_element:
                element_counted += 1
                previous_element = nums[index]

            # If we have counted 3 numbers then return current number.
            if element_counted == 3:
                return nums[index]

        # We never counted 3 distinct numbers, return largest number.
        return nums[0]
