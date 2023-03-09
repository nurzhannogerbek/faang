class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Approach 1:
        expected = sorted(heights)
        no_match = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                no_match += 1
        return no_match

        # Approach 2:
        # Time complexity: O(nlog(n)).
        # Space complexity: O(n).
        # no_match = 0
        # for (i, j) in zip(heights, sorted(heights)):
            # if i != j:
                # no_match += 1
        # return no_match
