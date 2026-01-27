class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        I am given a list of numbers that represent the amount of money on a street of houses. The houses are arranged in a circle, so the first
        house in the array is the neighbor of the last house in the array. If two adjacent houses are robbed, I cannot rob a given house as it
        will trigger an alarm.

        Consider the problem if there is only 1 house. The max money I can take is just the money from that house. If there are two houses,
        the money I can take is the max of the two houses. Note that I cannot rob both because they are adjacent. If there are 3 houses I can
        do the following. I need to check the houses starting from the first house. I can either choose to either rob the house, in which case
        the maximum amount of money I would have is equal to the money in the house plus the money I had after leaving the house two doors down,
        or I can choose to not rob the house in which case I have the same amount of money as I when I entered the house. Put formally,
        this can be represented by cur_money = max(house(n) + house(n-2), house(n-2)).

        Since the house are arranged circularly, I need to consider that the last house and first house are neighbors. This means I need
        to handle the edge case that I start at the first house and rob it, which means I cannot rob the last house. One thing I could do is to
        run the original algorithm for house robber twice, one excluding the first house and one excluding the last house. Then I take the max
        of these two runs as my final answer

        time: O(n)
        memory: O(n)
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Run search without first house
        max_cash_last = self._helper(nums[1:])
        # Run search without last house
        max_cash_first = self._helper(nums[:-1])
        return max(max_cash_last[-1], max_cash_first[-1])
        
    def _helper(self, arr):
        """
        Helper function takes array and runs house robber algorithm. Returns an array of the maximum amount of money possible at each house
        """
        if len(arr) == 1:
            return [arr[0]]
        if len(arr) == 2:
            return [max(arr[0], arr[1])]
        
        max_cash = [0] * len(arr)
        max_cash[0] = arr[0]
        max_cash[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            max_cash[i] = max(max_cash[i-2] + arr[i], max_cash[i-1])
        return max_cash
        
