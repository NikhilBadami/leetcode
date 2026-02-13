class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        I am given an integer array of nums and must return the longest strictly increasing subsequence. Strictly increasing means that each
        subsequent number must be greater than the last.

        I can solve this by iterating backwards over the array and finding the longest increasing subsequence starting from this number. I can
        then cache these results since this answer will not change based on earlier numbers. Then for earlier numbers, while iterating I can
        check each number greater than the current number and add 1 to its LIS. The answer is the largest value in the array.

        time: O(n^2)
        memory: O(n)
        """
        dp = [1] * len(nums)
        # Answer will be at least 1
        max_lis = 1

        for i in range(len(nums) - 1, -1, -1):
            cur_max = 1
            for j in range(i, len(nums)):
                # This array iterates forwards towards the end of the array
                if nums[j] > nums[i]:
                    cur_max = max(cur_max, dp[j] + 1)
            dp[i] = cur_max
            max_lis = max(cur_max, max_lis)
        return max_lis
        
