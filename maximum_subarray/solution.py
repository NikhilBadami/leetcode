class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The ask is to find the sub-array that has the maximum sub and return this value. While iterating through the array,
        I can see that if at some index, the number, or numbers preceeding this index are negative, I can disregard this
        negative prefix since it won't contribute anything to the overall solution. If the current index is positive, it would
        be better so simply consider the subarray that only includes this current index. This works even if the entire array
        is negative because adding negative numbers together only makes the solution smaller, so it would always be optimal
        to take the current index over a sum of negative values, or a negative prefix.

        time: O(n)
        memory: O(1)
        """
        max_sum = float("-inf")
        cur_sum = float("-inf")
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            i += 1
        return max_sum
        
