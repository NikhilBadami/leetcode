class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The idea is to find a day (index) in the array to buy a stock, and then find a subsequent index in the array to 
        sell the stock where I can make a profit. Consider the following example:

        [7,8,1,5,3,6,4]

        The naive solution would be to iterate over the entire array twice, checking the max profit from each index.
        A better way would be to use a sliding window to track the maximum profit starting from a particular index.
        As I iterate, if I encounter a value at the right pointer less than the less pointer, I reset the left pointer
        to the right pointer. The reason why is because I've found this index with a value less than my current buy
        day so I know that for any subsequent day, it would be more profitable to sell based on this new buy day
        than my current buy day. Any combination I can come up with with subsequent prices would always be more profitable
        with the lower price. Or as common sense would dicate, its always better to get a lower price.

        time: O(n)
        memory: O(1) --> Only need to allocate left and right pointers and result variable
        """
        l, r = 0, 0
        profit = -1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        return profit
        
