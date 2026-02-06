class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        I am given an array of numbers and need to find the product of the subarray that has the largest product.

        I can accomplish this by iterating through the array and tracking the various prods of subarrays up to and including the current element.
        Specifically, I need to track the minimum and maximum sums up to and including that array. This is because of the presence of negative
        numbers which can flip the sign of very negative products and make them very large positive numbers. Additionally, I need to handle
        encountering 0. If this happens, I simply reset my tracking variables to 1.

        time: O(n)
        memory: O(1)
        """
        max_sum = nums[0]
        cur_max = 1
        cur_min = 1
        for i in range(len(nums)):
            cur_max *= nums[i]
            cur_min *= nums[i]
            if nums[i] == 0:
                cur_max = 1
                cur_min = 1
                max_sum = max(0, max_sum)
            else:
                tmp = cur_max
                cur_max = max(cur_max, cur_min, nums[i])
                cur_min = min(tmp, cur_min, nums[i])
                max_sum = max(cur_max, max_sum)
        return max_sum
        
