class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The goal of the problem is to find the sub-array that yields the largest sum. One way to do this is to divide
        the array continuously down into individual elements based on the mid point of each sub array and then start
        taking sums. At each level of the divide tree, take the sum of the current sub-array, or one of its child
        divides. Whichever is larger. Return the overall result of this.

        time: dividing the array creates O(log(n)) calls. Looping over the array to find the sum takes at most O(n) time
              and this needs to be done at each divide
              overall: O(nlog(n))
        memory: O(log(n)) --> call stack and for number of array copies
        """
        return self.helper(nums)
    
    def helper(self, sub_nums) -> int:
        """
        Helper function handles divide and conquer
        """
        # Base case there is only one element
        if len(sub_nums) == 1:
            return sub_nums[0]
        
        # Find mid_pt of array
        mid_pt = len(sub_nums) // 2

        # Split the array
        left_sum = self.helper(sub_nums[:mid_pt])
        right_sum = self.helper(sub_nums[mid_pt:])

        # Get sum of current array
        t_sum = sum(sub_nums)

        # Return the largest sum
        split_sum_max = max(left_sum, right_sum)
        return max(split_sum_max, t_sum)

        
