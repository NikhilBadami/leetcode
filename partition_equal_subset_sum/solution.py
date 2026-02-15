class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        I am given an array nums and I need to determine if I can partition the array into two sub-arrays such that the sum of each sub-array is
        equal.

        I can make the observation that if the sum of the original array is odd, this problem is not solveable. Therefore, for any odd sum I
        immediately return False. For an even sum, my target is sum // 2. I can then interate backwards starting at the end of the array and
        add running sums to a set. If at any point the target is reached, I can return True. If not, return False.

        time: O(n * t) --> n is the number of elements, t is the number of unique sums
        memory: O(t)
        """
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2

        sums = set()
        sums.add(0)
        for i in range(len(nums) - 1, -1, -1):
            next_sums = set()
            for s in sums:
                t = s + nums[i]
                if t == target:
                    return True
                next_sums.add(t)
                next_sums.add(s)
            sums = next_sums
        return False
        
