class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Hint: This problem can be solved in O(n) time. Consider the trivial case of an array with only positive numbers.
        How would the solution be found? Now consider what happens when we introduce negative numbers. How does our
        iteration change when we encounter negative numbers? What happens to the sum that drives this decision making?

        For the trivial case, we would just add every number together. An array which only has positive number will have
        a maximum sum by adding all the numbers in the array. What happens if there are negative numbers in the array?
        If adding the current number to the sum of an existing sub array results in a number less than the current 
        number, start over with the current element as the current element is greater than the sum of the previous
        elements. This makes sense as a single element in the array is itself a sub-array. If this single element is
        greater than the sum of the previous n-1 elements, by definition this is the solution to the problem.
        If, however, the sum is greater than the current number, continue expanding the array even if the current element
        is negative.

        time: O(n)
        memory: O(1)
        """
        if len(nums) == 1:
            return nums[0]
        res = float(-inf)
        cur_sum = 0
        for n in nums:
            if cur_sum + n < n:
                cur_sum = n
            else:
                cur_sum += n
            res = max(cur_sum, res)
        return res
        
