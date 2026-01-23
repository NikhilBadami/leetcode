class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        I am given an array of numbers which represent the amount of money individual houses have. I need to determine the maximum amount of money
        I can take from these houses with the restriction that if two adjacent houses were broken into already, I cannot rob a given house.
        For example, in the array [1,2,3] if I rob houses 1 and 3 I cannot rob house 2.

        If I rob a house, this means that I cannot rob the houses next to it. Say I have an array [1]. The solution is obviously 1. If I have
        [1,2], the solution is 2. If I have [1,2,3], the solution is to rob houses 1 and 3. What if the array was [1,100,3]? The solution then
        would be to rob house 2 without robbing houses 1 or 3.

        I can have two base cases. For the first two houses, the amount of money I rob is based on max(house1, house2). What about house3?
        I need to determine if I should rob house 3. If I rob house 3, this means that I cannot rob house 2, so I rob house 1 in an attempt to
        maximize the amount of money I steal. I also have the option to not rob house 3, in which case the amount of money I have when I leave
        house 3 is the amount of money I have from robbing house 2. So this rule can be given by max(house3+house1, house2). Put more generally,
        for any given house n where n > 2, the maximum amount of money I could have after leaving that house is 
        max(house(n-2)+house(n), house(n-1)). In other words, at any given house, I choose to rob it if robbing this house and the house two
        houses down is more profitable than simply keeping the money from the house immediately before.

        time: O(n)
        memory: O(n)
        """
        # Base cases are for n = 1 and n = 2
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # For n > 2, we apply the rule from above
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_money[i] = max(nums[i] + max_money[i-2], max_money[i-1])
        return max_money[-1]
        
