class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        I am given an array of coin values and a target amount. I need to return the minimum number of coins needed to make up the amount.

        I can solve this problem as follows. I create an array where each index in the array represents an amount and the value at the index
        is the minimum number of coins needed to create that value. While iterating, I can take a coin value and subtract it from the current
        index to see if this value can be created. If so, I add 1 to that index's value. If not, I keep the value at -1. I return the last
        value in the array. For simplicity, the array will be 1-indexed (i.e., of size amount+1)
        
        time: O(n*c) --> n is the amount and c is the number of coins
        memory: O(n)
        """
        amounts = [-1] * (amount + 1)
        # Base cases where coin denominations exist in amounts array. The minimum way to create that value is to just use the coin
        # No coins are needed to make the value 0
        amounts[0] = 0
        for c in coins:
            if c < len(amounts):
                amounts[c] = 1
        for i in range(1, amount+1):
            # Iterate through coins to see what the smallest amount of coins needed are to make the current amount
            cur_min = float("inf")
            for c in coins:
                if i - c > 0:
                    if amounts[i-c] > 0:
                        cur_min = min(cur_min, amounts[i-c]+1)
            if cur_min != float("inf"):
                amounts[i] = cur_min if amounts[i] == -1 else min(cur_min, amounts[i])
        return amounts[-1]

