class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The goal is to find all combinations of three numbers that add to 0 in the input array. I can accomplish this by
        1: sorting the input and 2: scanning through the input for solutions. In an outer loop, I can scan through the
        array and select a number at nums[i]. I then subtract this number from 0, which becomes my target for the second
        loop. The second loop searches for two numbers that add to this target, essentially reducing to the solution for
        two-sum for a sorted input array. If I find a solution, then I append these three numbers to the result. One
        optimization is if I have a negative target but the numbers are all positive, I should end the overall loop as
        positive numbers will never sum to a negative number.

        I need to consider the possibility of duplicates as well. If there are duplicate numbers, every time I start the
        inner loop I will encounter the same solution first. What I should do is find every solution for this number
        and then skip duplicates in the outer loop.

        time: O(n^2)
        memory: O(m) --> m is the number of triplets that sum to 0
        """
        # Sort array
        nums.sort()

        res = []
        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            if target < 0:
                # All numbers after nums[i] are positive and will never sum to target
                break
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Ensure duplicates are skipped
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
        
