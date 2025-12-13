class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Goal is to maximize profit by selling the stock on a day where the price is higher than the day I bought it, in
        otherwords, max(sell_price - buy_price). A naive solution to this problem would be to iterate over the entire array
        for each possible price and record the maximum profit. This solution would be O(n^2).

        A better solution, however, would be to realize that while iterating, if I encounter a price that is lower than
        the current price I am consdiering, it makese sense to move my "buy day" to this price, as any sell price that
        comes after this would be greater assuming I buy on this cheaper day than the current day I am considering. By
        doing this I can reduce the run-time complexity of the algorithm to O(n)

        time: O(n)
        memory: O(1)
        """
        # Handle edge case where there is only one element in the prices array
        max_price = 0
        if len(prices) == 0:
            return max_price
        
        l, r = 0, 1
        while r < len(prices):
            max_price = max(max_price, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_price
        
