class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Hint: After sorting the array, how can we ensure we are not processing duplicates?

        Need to find all triplets in the array such that the sum is 0 and the indices are unique. The final solution cannot
        contain duplicate triplets.

        The first step of this solution is to sort the array. The reason for this is as we iterate through the array,
        we create a target, 0 - nums[i], and then pass this to a function 2-sum-array-is-sorted, the solution for which
        is already known. The input could have multiple of the same number and we need to make sure we do not process
        duplicate triplets. Say we had the following array: [-3,-3,0,1,2,3]. This array has the following solutions:
        [-3,0,3] and [-3,1,2]. The problem here is if we start the two-sum solution from the beginning from each -3,
        we will encounter the same solution first each time, namely [0,3]. Howerver, we can run the two-sum solution
        in such a way that we find all possible solutions for this number, and then skip all duplicates in the main loop,
        thus ensuring that we do not create duplicate triplets. Another efficiency is possible as well: after sorting,
        once the input number is greater than 0, there is no reason to continue processing because positive numbers cannot
        sum to 0.

        Two sum solution:

        Using the sorted array, create a left and right pointer at the start and end of the array. If the sum of nums[l]
        + nums[r] is too large, decrement the right pointer and if it is too small, increment the left pointer. We need
        to make a modification to this algorithm for this problem to ensure we are finding all unique solutions. Once
        we have found a single solution, we can either decrement the right pointer or increment the left pointer. If the
        next number is the same as the previous number, keep moving the pointer until it is a different number or it
        passes the other pointer. In the outer loop, move the pointer until the number is different.

        time: O(nlog(n)) to sort the array
              O(n^2) worst case to process the sorted array
        memory: O(n) --> 2n technicaly, n memory to sort and n memory to store solution
        """
        # Sort the input array
        nums.sort()

        # Iterate through sorted array
        res = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                # There are no other possible solutions
                break
            target = 0 - nums[i]
            # Search for all solutions that sum to target using the 2-sum solution for sorted arrays
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    # We have found a possible solution
                    res.append([nums[i], nums[l], nums[r]])
                    # We choose to increment the left pointer. We need to do this until we find a new number or the left
                    # pointer passes the right pointer
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
            # Since we have already retrieved all solutions for nums[i], we need to skip any duplicate occurrences
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1    
        return res

